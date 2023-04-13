class RequestParams:
    
    def __init__(self, extra_params: dict, token: str= '2e8ee9c554ecabfed1f064d76c8fbaa6', sport: str= 'baseball_mlb', regions: str = 'us'):
        self.token = token
        self.sport = sport
        self.regions = regions
        self.extra_params = extra_params