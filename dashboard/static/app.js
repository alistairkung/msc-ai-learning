/* Progressive enhancement for a static, source-backed learning record. */
'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const data = JSON.parse($('atlas-data').textContent);
  const rows = [...document.querySelectorAll('#topic-rows tr')];
  const tabs = [...document.querySelectorAll('[data-view]')];
  let previousFocus = null;
  let previousHash = '';

  function filter() {
    const query = $('search').value.trim().toLowerCase();
    const area = $('domain').value;
    const kind = $('kind').value;
    let count = 0;
    rows.forEach(row => {
      const match = row.dataset.search.includes(query) &&
        (area === 'all' || row.dataset.area === area) &&
        (kind === 'all' || (kind === 'focus' ? row.dataset.focus === 'true' : row.dataset.kind === kind));
      row.hidden = !match;
      if (match) count++;
    });
    $('count').textContent = `${count} of ${rows.length} recorded targets`;
    $('empty').hidden = count !== 0;
  }
  function showView(id, focus = false) {
    if (!tabs.some(tab => tab.dataset.view === id)) id = 'knowledge';
    tabs.forEach(tab => {
      const selected = tab.dataset.view === id;
      tab.setAttribute('aria-selected', String(selected));
      tab.tabIndex = selected ? 0 : -1;
      $(tab.dataset.view).hidden = !selected;
      if (selected && focus) tab.focus();
    });
  }
  function openTopic(id) {
    const topic = data.details[id];
    if (!topic) return;
    if (!$('detail').open) {
      previousFocus = document.activeElement;
      previousHash = location.hash.startsWith('#record-') ? '#knowledge' : location.hash;
    }
    $('detail-domain').textContent = topic.area;
    $('detail-title').textContent = topic.title;
    // HTML was escaped and validated by the Python generator; no raw source is evaluated.
    $('detail-body').innerHTML = topic.html;
    if (!$('detail').open) $('detail').showModal();
    $('detail-close').focus();
    history.replaceState(null, '', `#record-${id}`);
  }
  function handleHash() {
    const hash = location.hash.slice(1);
    if (hash.startsWith('record-')) openTopic(hash.slice(7));
    else showView(hash || 'knowledge');
  }
  document.addEventListener('click', event => {
    const link = event.target.closest('[data-open]');
    if (link) { event.preventDefault(); openTopic(link.dataset.open); }
  });
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
      showView(tab.dataset.view);
      history.replaceState(null, '', `#${tab.dataset.view}`);
    });
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) {
        event.preventDefault();
        showView(tabs[next].dataset.view, true);
        history.replaceState(null, '', `#${tabs[next].dataset.view}`);
      }
    });
  });
  ['search', 'domain', 'kind'].forEach(id => $(id).addEventListener(id === 'search' ? 'input' : 'change', filter));
  // Searching the map should not silently exclude topics outside the default focus.
  $('search').addEventListener('input', () => {
    if ($('search').value.trim() && $('kind').value === 'focus') { $('kind').value = 'all'; filter(); }
  });
  $('reset').addEventListener('click', () => {
    $('search').value = ''; $('domain').value = 'all'; $('kind').value = 'all'; filter();
  });
  $('detail-close').addEventListener('click', () => $('detail').close());
  $('detail').addEventListener('close', () => {
    history.replaceState(null, '', previousHash || '#knowledge');
    if (previousFocus && previousFocus.isConnected) previousFocus.focus();
  });
  $('quality-btn').addEventListener('click', () => $('quality').showModal());
  $('quality-close').addEventListener('click', () => $('quality').close());
  // Recency changes in the browser even when Pages has not rebuilt recently.
  const today = new Date();
  const age = Math.max(0, Math.floor((today - new Date(`${data.meta.reviewed_on}T00:00:00Z`)) / 86400000));
  const freshness = age > data.meta.stale_after_days
    ? `Record review is ${age} days old — check for newer learning evidence`
    : `Reviewed ${data.meta.reviewed_on} · evidence through ${data.meta.evidence_through}`;
  $('freshness').textContent = freshness;
  $('quality-freshness').textContent = `${freshness}. Age is a review prompt, not a claim that knowledge has decayed.`;
  document.querySelectorAll('[data-event]').forEach(node => {
    if (!node.dataset.event) return;
    const elapsed = Math.floor((today - new Date(`${node.dataset.event}T00:00:00Z`)) / 86400000);
    if (elapsed > data.meta.stale_after_days) node.textContent += ' · older evidence';
  });
  document.documentElement.classList.add('js');
  showView('knowledge');
  filter();
  handleHash();
  window.addEventListener('hashchange', handleHash);
})();
