import requests
import json
from module.constants import ODDS_API_URL
from module.models.request_param import RequestParams
from module.models.response_object import GameObject


def call_api_handler():
    request_params = RequestParams(token='2e8ee9c554ecabfed1f064d76c8fbaa6', regions= 'us', sport='baseball_mlb', extra_params={})
    response_dict = call_api(ODDS_API_URL, request_params)
    response_object = build_response_object(response_dict)

    return response_object


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
                result = response.json()
                break
    except Exception:
        raise Exception("API CALL FAILED")
    return result


def build_response_object(response_dict: dict) -> [GameObject]:
    games_list = []
    for games in response_dict:
        game_object = GameObject(response_dict['home_team'], response_dict['away_team'])
        bookmakers =  response_dict['bookmakers']
        game_object.build_point_spread(bookmakers)
        games_list.append(game_object)
    return games_list

#TODO def Build extra params