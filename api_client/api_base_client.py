from api_client.api_requests_client import ApiRequestClient
from utilities.config_parser import get_base_uri


class BaseClient:

    def __init__(self):
        self.base_uri = get_base_uri()
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': f'{self.base_uri[8:]}',
            'User-Agent': 'Mozilla / 5.0(Macintosh;Intel Mac OS X 10_15_7) AppleWebKit / 605.1.15 (KHTML, like Gecko) '
                          'Version / 16.2 Safari / 605.1.15',
            'Accept-Language': 'en - IN, en - GB;q = 0.9, en;q = 0.8',
            'Referer': f'{self.base_uri}'
        }
        self.api_rest_client = ApiRequestClient()
