
import pandas as pd
from typing import List, Dict


def build_response_handler(response_json) -> pd.DataFrame:
    games_list = build_response_object(response_json)
    df = pd.DataFrame(games_list)

    df['commence_time'] = pd.to_datetime(df['commence_time']).dt.tz_convert(tz='US/Eastern').dt.strftime('%I:%M %p')
    df['lst_uptd'] = pd.to_datetime(df['lst_uptd']).dt.tz_convert(tz='US/Eastern')
    return df


def build_response_object(response_dict: dict) -> List[Dict]:
    games_list = []
    for game in response_dict:
        game_object = {'id':            game['id'],
                       'home_team':     game['home_team'],
                       'away_team' :    game['away_team'],
                       'commence_time': game['commence_time']}
        bookmakers =  game['bookmakers']
        rows_with_odds_included = build_oddsmaker_row(game_object, bookmakers)
        games_list.extend(rows_with_odds_included)
    return games_list


def build_oddsmaker_row(game_object: dict, bookmakers: list) -> List[Dict]:
    return_list = []
    for bookmaker in bookmakers:
        copy_game_object = game_object.copy()
        oddsmaker = bookmaker['title']
        last_updated =  bookmaker['last_update']
        outcomes = bookmaker['markets'][0]['outcomes']
        home_odds = away_odds = 0
        for outcome in outcomes:
            if outcome['name'] == copy_game_object['home_team']:
                home_odds = outcome['price']
            else:
                away_odds = outcome['price']
        odds_row = {'odds_maker':   oddsmaker,
                    'home_odds':    home_odds,
                    'away_odds':    away_odds,
                    'lst_uptd':     last_updated
                    }
        copy_game_object.update(odds_row)
        return_list.append(copy_game_object)
    return return_list

