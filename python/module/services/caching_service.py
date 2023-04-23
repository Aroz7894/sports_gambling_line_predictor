import os
import json
from module.models.request_param import RequestParams


#In future Can use built in caching functions like functools and/or @lru_cache to cache. But since this is a
# single running script at this point it wont hold memory. so instead i will write to file.    
WRITE_PATH = 'cached_api_response.json'


def cache_response(func):
    def wrapper_func(api_url: str, params: RequestParams):
        cache_key = f'{params.sport}:{params.regions}'
        with open(WRITE_PATH, 'r+') as cache_file:
            cache = {} 
            print(cache_file.read() == '')
            if cache_file.read():
                cache = json.load(cache_file)
            if cache.get(cache_key) is not None:
                api_response = cache[cache_key]
                print('USING CACHED RESPONSE')
            else:
                print('NOT USING CACHED RESPONSE')
                api_response = func(api_url, params)
                cache[cache_key] = api_response
                cache_file.write(json.dumps(cache))
        return api_response
    return wrapper_func


def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


#TO DO Evict Cache 