from api_client.api_base_client import BaseClient
from endpoints import pet


class Pet(BaseClient):

    def __init__(self):
        super().__init__()

    def add_pet(self, pet_data):
        url = self.base_uri + pet.pet_endpoints['ADD_OR_UPDATE_PET']
        response = self.api_rest_client.post(url=url, payload=pet_data, headers=self.headers)
        return response

    def update_pet(self):
        pass

    def find_pet_by_status(self):
        pass

    def find_pet_by_tags(self):
        pass

    def find_pet_by_id(self):
        pass

    def update_pet_by_id(self):
        pass

    def delete_pet_by_id(self):
        pass

    def upload_image_of_pet(self):
        pass
