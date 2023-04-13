from module.services.call_api_service import call_api_handler
from module.services.build_response_service import build_response_handler


def handler():
    return_json = call_api_handler()
    df = build_response_handler(return_json)
    print(df)


if __name__ == "__main__":
    handler()
