import pandas as pd

from exercises.lesson23_linear_regression import (
    run_regression_pipeline,
)


def make_houses():
    return pd.DataFrame(
        {
            "size": [
                500,
                600,
                700,
                800,
                900,
                1000,
                1100,
                1200,
                1300,
                1400,
                1500,
                1600,
                1700,
                1800,
                1900,
                2000,
                2100,
                2200,
                2300,
                2400,
            ],
            "bedrooms": [
                1,
                1,
                1,
                2,
                2,
                2,
                2,
                3,
                3,
                3,
                3,
                3,
                4,
                4,
                4,
                4,
                4,
                5,
                5,
                5,
            ],
            "age": [
                30,
                25,
                20,
                20,
                18,
                15,
                14,
                12,
                10,
                9,
                8,
                7,
                6,
                5,
                5,
                4,
                3,
                3,
                2,
                1,
            ],
            "price": [
                150,
                170,
                190,
                220,
                240,
                270,
                290,
                320,
                350,
                370,
                400,
                420,
                450,
                480,
                500,
                530,
                550,
                580,
                610,
                640,
            ],
        }
    )


def test_run_regression_pipeline():
    houses = make_houses()

    result = run_regression_pipeline(houses)

    assert set(result.keys()) == {
        "model",
        "predictions",
        "actual",
        "mae",
        "mse",
        "r2",
    }

    assert len(result["predictions"]) == 4
    assert len(result["actual"]) == 4

    assert result["mae"] >= 0
    assert result["mse"] >= 0
    assert result["r2"] <= 1

    assert hasattr(result["model"], "coef_")
    assert hasattr(result["model"], "intercept_")
