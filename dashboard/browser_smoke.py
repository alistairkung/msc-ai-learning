"""Run separately from pytest; requires Playwright + Chromium. No model calls."""
import argparse
import os
from pathlib import Path
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

from playwright.sync_api import sync_playwright, expect


@contextmanager
def serve(site):
    handler = partial(SimpleHTTPRequestHandler, directory=str(site.resolve()))
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{server.server_port}'
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def check(site: Path, screenshots: Path | None = None) -> None:
    with serve(site) as origin, sync_playwright() as p:
        url = origin + '/index.html'
        browser = p.chromium.launch(headless=True, executable_path=os.environ.get('PLAYWRIGHT_CHROMIUM_EXECUTABLE'))
        page = browser.new_page(viewport={'width': 1440, 'height': 1000})
        errors, remote = [], []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('request', lambda request: remote.append(request.url) if request.url.startswith(('http:', 'https:')) and not request.url.startswith(origin + '/') else None)
        page.goto(url)
        expect(page.locator('#knowledge')).to_be_visible()
        expect(page.locator('#runway')).not_to_be_visible()
        assert page.locator('#topic-rows tr:visible').count() > 0
        page.locator('#search').fill('nothing-matches-this-string')
        expect(page.locator('#empty')).to_be_visible()
        page.locator('#reset').click()
        count = page.locator('#topic-rows tr').count()
        assert page.locator('#topic-rows tr:visible').count() == count
        page.locator('#kind').select_option('independent')
        assert page.locator('#topic-rows tr:visible').count() == 1
        trigger = page.locator('#topic-rows [data-open="bfs"]').first
        trigger.click()
        expect(page.locator('#detail')).to_be_visible()
        expect(page.locator('#detail-title')).to_have_text('BFS')
        assert page.locator('#detail .sources a').count() > 0
        page.keyboard.press('Escape')
        expect(page.locator('#detail')).not_to_be_visible()
        expect(trigger).to_be_focused()
        page.locator('#tab-knowledge').focus()
        page.keyboard.press('ArrowRight')
        expect(page.locator('#runway')).to_be_visible()
        assert page.locator('#tab-runway').get_attribute('aria-selected') == 'true'
        for summary in page.locator('.course > details > summary').all():
            summary.click()
        expect(page.get_by_text('GD + convergence analysis', exact=True)).to_be_visible()
        assert page.get_by_text('Convergence analysis', exact=True).count() > 0
        expect(page.get_by_text('Project presentation', exact=True)).to_be_visible()
        page.locator('#tab-queue').click()
        assert page.locator('.queue-col').count() == 3
        page.locator('#tab-knowledge').click()
        page.locator('#reset').click()
        page.locator('#domain').select_option('Agentic systems')
        assert page.locator('#topic-rows tr:visible').count() == 2
        page.locator('#reset').click()
        page.locator('#kind').select_option('focus')
        if screenshots:
            screenshots.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(screenshots/'atlas-desktop.png'), full_page=True)
        page.set_viewport_size({'width': 390, 'height': 844})
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
        page.locator('#topic-rows [data-open="ucs"]').first.click()
        expect(page.locator('#detail')).to_be_visible()
        assert page.locator('#detail').bounding_box()['width'] <= 390
        page.keyboard.press('Escape')
        if screenshots:
            page.screenshot(path=str(screenshots/'atlas-mobile.png'), full_page=True)
        page.goto(url+'#record-mle')
        expect(page.locator('#detail-title')).to_have_text('Likelihood / MLE')
        fallback = browser.new_context(java_script_enabled=False)
        plain = fallback.new_page()
        plain.goto(url)
        expect(plain.locator('#record-bfs')).to_be_visible()
        expect(plain.locator('#runway')).to_be_visible()
        assert plain.locator('#topic-rows tr').count() == count
        assert not remote, remote
        assert not errors, errors
        fallback.close()
        browser.close()
    print('Browser checks passed: filters, details, keyboard, mobile, deep links and no-JS fallback.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    parser.add_argument('--screenshots', type=Path)
    args = parser.parse_args()
    check(args.site, args.screenshots)
