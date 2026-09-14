"""Optional adapter for running the readable example against TaxCalcBench.

The learning repo does not vendor TaxCalcBench. Clone it separately and pass
its path to ``load_benchmark_context``.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys

from .lecturer_case import CASE_NAME


@dataclass
class BenchmarkContext:
    case_name: str
    taxpayer_json: str
    taxpayer: dict
    expected_xml: str
    form_lines: list[str]
    line_keys: list[str]
    form_text: str
    evaluator: object

    @property
    def labels(self) -> dict[str, str]:
        return dict(zip(self.line_keys, self.form_lines))

    def render_return(self, filing_status: str, lines: dict[str, int]) -> str:
        """Render structured line values in the text format expected by the benchmark."""
        output = [
            "Form 1040: U.S. Individual Income Tax Return",
            "=" * 43,
            f"Filing Status: {filing_status}",
        ]

        for line_key in self.line_keys:
            value = lines.get(line_key, 0)
            output.append(f"{self.labels[line_key]} | | {value}")

        return "\n".join(output)

    def grade(self, return_text: str, verbose: bool = True) -> str:
        """Call the official TaxCalcBench evaluator, matching the tutorial."""
        result = self.evaluator.evaluate(
            return_text,
            self.expected_xml,
            tax_year="ty24",
        )

        if result.strictly_correct_return:
            verdict = "strict"
        elif result.lenient_correct_return:
            verdict = "lenient"
        else:
            verdict = "wrong"

        if verbose:
            failed_lines = [
                line
                for line in result.report.splitlines()
                if "✗" in line
            ]
            print("\n".join(failed_lines) or "all graded lines correct")
            print(
                "strict:",
                result.strictly_correct_return,
                "lenient:",
                result.lenient_correct_return,
                "strict by line:",
                f"{result.correct_by_line_score:.0%}",
                "lenient by line:",
                f"{result.lenient_correct_by_line_score:.0%}",
            )

        return verdict


def load_benchmark_context(
    tax_calc_bench_root: str | Path,
    case_name: str = CASE_NAME,
) -> BenchmarkContext:
    """Load the same TaxCalcBench case/resources used in the tutorial notebook."""
    benchmark_root = Path(tax_calc_bench_root).resolve()

    if str(benchmark_root) not in sys.path:
        sys.path.insert(0, str(benchmark_root))

    from tax_calc_bench.tax_return_evaluator import TaxReturnEvaluator
    from tax_calc_bench.ty24_prompt import TAX_RETURN_GENERATION_PROMPT

    case_directory = (
        benchmark_root
        / "tax_calc_bench"
        / "ty24"
        / "test_data"
        / case_name
    )

    taxpayer_json = (case_directory / "input.json").read_text()
    expected_xml = (case_directory / "output.xml").read_text()
    taxpayer = json.loads(taxpayer_json)

    form_lines = [
        line.split(" | ")[0].strip()
        for line in TAX_RETURN_GENERATION_PROMPT.splitlines()
        if re.match(r"Line \d", line) and "[Description]" not in line
    ]
    line_keys = [
        re.match(r"Line (\w+):", line).group(1)
        for line in form_lines
    ]

    return BenchmarkContext(
        case_name=case_name,
        taxpayer_json=taxpayer_json,
        taxpayer=taxpayer,
        expected_xml=expected_xml,
        form_lines=form_lines,
        line_keys=line_keys,
        form_text="\n".join(form_lines),
        evaluator=TaxReturnEvaluator(),
    )
