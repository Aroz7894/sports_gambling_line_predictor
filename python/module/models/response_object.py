from module.models.outcome_object import OddsObject


class GameObject():
    home_team = ''
    away_team = ''
    point_spreads = []

    def __init__(self, home_team:str, away_team:str):
        self.home_team = home_team
        self.away_team = away_team

    def build_point_spread(self, bookmakers: list):
        for bookmaker in bookmakers:
            name = bookmaker['title']
            outcomes = bookmaker['markets']['outcomes']
            for outcome in outcomes:
                home_odds = 0
                away_odds = 0
                if outcome['name'] == self.home_team:
                    home_odds = outcome['price']
                else:
                    away_odds = outcome['price']
                outcome_object = (name, home_odds, away_odds)
                self.point_spreads.append(outcome_object) 

    #TODO
    # def __print__()