"""Compact artifacts from the lecturer's TaxCalcBench example.

These values mirror the printed inventory/placement artifacts for the
`single-w2-unemployment-1099g` case in FTEC5660 Tutorial 1.

The raw TaxCalcBench input JSON is intentionally not copied here; use
`benchmark_adapter.py` to load it from a local benchmark checkout.
"""

CASE_NAME = "single-w2-unemployment-1099g"

INVENTORY = {
    "filing_status": "single",
    "date_of_birth": "1973-10-14",
    "boxes": [
        {
            "document": "W-2 #1",
            "box": "Box 1",
            "what": "Wages, tips, other compensation",
            "amount": 145_000,
        },
        {
            "document": "W-2 #1",
            "box": "Box 2",
            "what": "Federal income tax withheld",
            "amount": 12_000,
        },
        {
            "document": "W-2 #1",
            "box": "Box 3",
            "what": "Social security wages",
            "amount": 132_900,
        },
        {
            "document": "W-2 #1",
            "box": "Box 4",
            "what": "Social security tax withheld",
            "amount": 8_240,
        },
        {
            "document": "W-2 #1",
            "box": "Box 5",
            "what": "Medicare wages and tips",
            "amount": 145_000,
        },
        {
            "document": "W-2 #1",
            "box": "Box 6",
            "what": "Medicare tax withheld",
            "amount": 2_103,
        },
        {
            "document": "W-2 #1",
            "box": "State wages, tips, etc.",
            "what": "State wages, tips, etc.",
            "amount": 1,
        },
        {
            "document": "1099-G #1",
            "box": "Box 1",
            "what": "Unemployment compensation",
            "amount": 12_345,
        },
        {
            "document": "1099-G #1",
            "box": "Box 4",
            "what": "Federal income tax withheld",
            "amount": 1_235,
        },
    ],
}

PLACEMENTS = [
    {
        "document": "W-2 #1",
        "box": "Box 1",
        "amount": 145_000,
        "entered_on": "Form 1040 line 1a",
        "line": "1a",
        "why": "W-2 wages are entered on line 1a.",
    },
    {
        "document": "W-2 #1",
        "box": "Box 2",
        "amount": 12_000,
        "entered_on": "Form 1040 line 25a",
        "line": "25a",
        "why": "Federal income tax withheld from W-2 is entered on line 25a.",
    },
    {
        "document": "W-2 #1",
        "box": "Box 3",
        "amount": 132_900,
        "entered_on": "none",
        "line": "none",
        "why": "Social security wages are not directly entered on Form 1040.",
    },
    {
        "document": "W-2 #1",
        "box": "Box 4",
        "amount": 8_240,
        "entered_on": "none",
        "line": "none",
        "why": "Social security tax withheld is not directly entered on the main form.",
    },
    {
        "document": "W-2 #1",
        "box": "Box 5",
        "amount": 145_000,
        "entered_on": "none",
        "line": "none",
        "why": "Medicare wages are not directly entered on Form 1040.",
    },
    {
        "document": "W-2 #1",
        "box": "Box 6",
        "amount": 2_103,
        "entered_on": "none",
        "line": "none",
        "why": "Medicare tax withheld is not directly entered on the main form.",
    },
    {
        "document": "W-2 #1",
        "box": "State wages, tips, etc.",
        "amount": 1,
        "entered_on": "none",
        "line": "none",
        "why": "State wages are not entered on federal Form 1040.",
    },
    {
        "document": "1099-G #1",
        "box": "Box 1",
        "amount": 12_345,
        "entered_on": "Schedule 1 line 7",
        "line": "8",
        "why": "Unemployment compensation flows through Schedule 1 to line 8.",
    },
    {
        "document": "1099-G #1",
        "box": "Box 4",
        "amount": 1_235,
        "entered_on": "Form 1040 line 25b",
        "line": "25b",
        "why": "Federal withholding from the 1099-G is entered on line 25b.",
    },
]

EXPECTED_KEY_LINES = {
    "1a": 145_000,
    "9": 157_345,
    "11": 157_345,
    "12": 14_600,
    "15": 142_745,
    "16": 27_301,
    "25d": 13_235,
    "37": 14_066,
}
