from pprint import pprint

import requests

from endpoints.pet import pet_endpoints
from utilities import config_parser
from assertpy.assertpy import assert_that


def test_finding_pet_by_id():
    response = requests.get(
        config_parser.get_base_uri() + pet_endpoints['GET_UPDATE_OR_DELETE_PET_BY_ID'].replace("{petId}", "1"))
    response_text = response.json()
    pprint(response_text)
    assert_that(response.status_code).is_equal_to(200)
