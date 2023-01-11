from pprint import pprint

import requests
from utilities import config_parser
from endpoints import http_methods_endpoints
from assertpy.assertpy import assert_that


def test_get_method():
    response = requests.get(config_parser.get_base_uri() + http_methods_endpoints.http_methods_endpoints['GET'])
    response_text = response.json()
    pprint(response_text)
    assert_that(response.status_code).is_equal_to(200)
