import requests
import json
import pandas as pd
from typing import List
from module.constants import ODDS_API_URL
from module.models.request_param import RequestParams
from module.models.response_object import GameObject


def call_api_handler() -> pd.DataFrame:
    request_params = RequestParams(extra_params={})
    response_json = call_api(ODDS_API_URL, request_params)
    game_list = build_response_object(response_json)
    reponse_list = []
    for game in game_list:
        reponse_list.extend(game.to_dict())
    return pd.DataFrame(reponse_list)


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


def build_response_object(response_dict: dict) -> List[GameObject]:
    games_list = []
    for game in response_dict:
        game_object = GameObject(game['home_team'], game['away_team'], game['commence_time'])
        bookmakers =  game['bookmakers']
        game_object.build_point_spread(bookmakers)
        games_list.append(game_object)
    return games_list

#TODO def Build extra params