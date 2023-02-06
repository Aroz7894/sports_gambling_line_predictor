import requests
import json
from module.constants import ODDS_API_URL
from module.models.request_param import RequestParams


def call_api_handler():
    request_params = RequestParams(token='2e8ee9c554ecabfed1f064d76c8fbaa6', regions= 'us', sport='americanfootball_nfl', extra_params={})
    response_dict = call_api(ODDS_API_URL, request_params)
    return response_dict

def call_api(base_url: str, params: RequestParams) -> dict: 
    retry = 0
    result = ''
    url = base_url.format(token=params.token, regions=params.regions, sport=params.sport)
    print(url)
    try:
        while retry < 3:        
            response = requests.get(url)
            if response.status_code != 200:
                print(response.status_code)
                retry += 1
            else: 
                result = response.json()[0]
                break
    except Exception:
        raise Exception("API CALL FAILED")
    return result


#TODO def Build extra params