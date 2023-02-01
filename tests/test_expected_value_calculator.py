import pytest
from module.expected_value_calculator import convert_amer_odds_to_decimal, calculate_expected_value, profit_calculator


def test_convert_amer_odds_to_decimal():
    amer_odds = convert_amer_odds_to_decimal(-150)
    assert amer_odds == 1.667
    amer_odds = convert_amer_odds_to_decimal(110)
    assert amer_odds == 2.1
    amer_odds = convert_amer_odds_to_decimal(0)
    assert amer_odds == 0


def test_profit_calculator():
    profit = profit_calculator(2.1, 100)
    assert profit == 110
    profit = profit_calculator(7.0, 100)
    assert profit == 600
