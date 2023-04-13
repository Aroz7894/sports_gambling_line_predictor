from module.models.outcome_object import OddsObject
from typing import List, Dict


class GameObject():
    home_team = ''
    away_team = ''
    commence_time = ''
    point_spreads:List[OddsObject] = list()

    def __init__(self, home_team:str, away_team:str, commence_time):
        self.home_team = home_team
        self.away_team = away_team
        self.commence_time = commence_time

    def build_point_spread(self, bookmakers: list):
        for bookmaker in bookmakers:
            name = bookmaker['title']
            last_updated =  bookmaker['last_update']
            outcomes = bookmaker['markets'][0]['outcomes']
            home_odds = away_odds = 0
            for outcome in outcomes:
                if outcome['name'] == self.home_team:
                    home_odds = outcome['price']
                else:
                    away_odds = outcome['price']
            outcome_object = OddsObject(name, home_odds, away_odds, last_updated)
            self.point_spreads.append(outcome_object) 

    def to_dict(self) -> List[Dict]:
        return_list = []
        for row in self.point_spreads:
            teams_dict = {'home_team': self.home_team,
                          'away_team': self.away_team,
                          'commence_time': self.commence_time}
            teams_dict.update(row.to_dict())
            return_list.append(teams_dict)
        # print(return_list)
        return return_list
