import requests, urllib.parse
from exceptions import *
from config.apiCfg import ApiConfig


class API:
    def __init__(self, api_cfg: ApiConfig) -> None:
        self.url = 'https://codeforces.com/api/'
        self.ok_status = 'OK'
        self.ok_code = 200
        self.json_response = dict()
        self.cfg = api_cfg
        self.request_result = requests.Response

    def handle_misc_errors(self) -> None:
        if self.request_result.status_code != self.ok_code:
            raise InternalAPIErrorException

    def request_to_json(self) -> dict:
        result = self.request_result.json()
        if result['status'] != self.ok_status:
            raise InternalAPIErrorException
        return result['result']

    def request(self, method: str, args: dict) -> dict | list:
        full_request_url = self.url + method + urllib.parse.urlencode(args)
        try:
            self.request_result = requests.get(url=full_request_url, timeout=self.cfg.timeout)
        except requests.ConnectionError:
            raise RequestConnectionErrorException('User not connected to the internet')
        except requests.Timeout:
            raise RequestTimeoutException(f'Request to {full_request_url} exceeded time limit of {self.cfg.timeout}s')
        except Exception:
            raise UndefinedAPIErrorException(f'Unknown error occured when requesting to {full_request_url}')

        self.handle_misc_errors()

        return self.request_to_json()
    
    def page_request(self, url: str) -> str:
        try:
            self.request_result = requests.get(url=url, timeout=self.cfg.timeout)
        except requests.ConnectionError:
            raise RequestConnectionErrorException('User not connected to the internet')
        except requests.Timeout:
            raise RequestTimeoutException(f'Request to {url} exceeded time limit of {self.cfg.timeout}s')
        except Exception:
            raise UndefinedAPIErrorException(f'Unknown error occured when requesting to {url}')
        
        return self.request_result.content