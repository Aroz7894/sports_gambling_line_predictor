import requests
from module.constants import ODDS_API_URL
from module.models.request_param import RequestParams


def call_api_handler() -> dict:
    request_params = RequestParams(extra_params={})
    return call_api(ODDS_API_URL, request_params)


def call_api(base_url: str, params: RequestParams) -> dict: 
    retry = 0
    result = ''
    url = base_url.format(token=params.token, regions=params.regions, sport=params.sport)
    try:
        while retry < 3:        
            response = requests.get(url)
            if response.status_code != 200:
                print(response.status_code)
                retry += 1
            else: 
                result = response.json()
                break
    except Exception:
        raise Exception("API CALL FAILED")
    return result


#TODO def Build extra params