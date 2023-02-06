class RequestParams:
    
    def __init__(self, token: str, sport: str, regions: str, extra_params: dict ):
        self.token = token
        self.sport = sport
        self.regions = regions
        self.extra_params = extra_params
