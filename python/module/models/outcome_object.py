class OddsObject():
    odds_maker = ''
    home_odds = 0
    away_odds = 0
    home_ev = 0
    away_ev = 0
    lst_uptd = ''

    def __init__(self, odds_maker, home_odds, away_odds, lst_uptd):
        self.odds_maker = odds_maker
        self.home_odds = home_odds
        self.away_odds = away_odds
        self.lst_uptd = lst_uptd

    def to_dict(self):
        return {'odds_maker': self.odds_maker,
                'home_odds' : self.home_odds,
                'away_odds' : self.away_odds,
                'home_ev'   : self.home_ev,
                'away_ev'   : self.away_ev,
                'lst_uptd'  : self.lst_uptd
        }

    #TODO
    #def calculate_ev()
 
