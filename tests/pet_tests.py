import json
from pprint import pprint

import requests

from data.pet import PetData
from endpoints.pet import pet_endpoints
from models.pet import Pet
from utilities import config_parser
from assertpy.assertpy import assert_that


def test_finding_pet_by_id():
    response = requests.get(
        config_parser.get_base_uri() + pet_endpoints['GET_UPDATE_OR_DELETE_PET_BY_ID'].replace("{petId}", "2"),
        headers={"accept": "application/json"})
    response_text = response.json()
    pprint(response_text)
    assert_that(response.status_code).is_equal_to(200)


def test_adding_a_pet():
    pet_model = Pet()
    pet_data = json.dumps(PetData(id=12,
                                  name="DoggieJi",
                                  category={"id": 1, "name": "Dogs"},
                                  photoUrls=[""],
                                  tags=[{"id": 0, "name": "string"}],
                                  status="available"), default=vars)

    response = pet_model.add_pet(pet_data)
    pprint(response.text)
    assert_that(response.status_code).is_equal_to(200)
