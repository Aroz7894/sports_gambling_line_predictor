
# expected value = (fair win probability) x (profit if win) - (fair loss probability) x (stake)
# The implied win percentage can be from a sports betting model or calculated using the no vig “fair” odds from a sharp sportsbook.
# Finding the no vig “fair” odds from the sharpest sportsbook in the world (you know what it is!) is the industry standard for fair win probability.
def calculate_expected_value(fair_win_prob: float, stake: float, odds: float):
    if abs(odds) > 100:
        odds = convert_amer_odds_to_decimal(odds)
    ev = (fair_win_prob * profit_calculator(odds, stake)) - \
        ((1-fair_win_prob)*stake)
    return round(ev, 2)


def profit_calculator(odds: float, stake: float):
    return (odds * stake) - stake


def convert_amer_odds_to_decimal(amer_odds: int):
    decimal_odds = 0
    if amer_odds > 0:
        decimal_odds = amer_odds/100 + 1
    elif amer_odds < 0:
        decimal_odds = 100/abs(amer_odds) + 1
    return round(decimal_odds, 5)
