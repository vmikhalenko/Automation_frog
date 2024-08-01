# creating framework

import requests
from endpoints.endpoints_handler import Endpoint

class GetObjectEndpoint(Endpoint):
    def get_one_obj_by_id(self, id):
        response = requests.get(f'https://api.restful-api.dev/objects/{id}')
        self.status = response.status_code
        self.id = response.json()['id']
        return response.json()['id']

    def check_id_same_as_sent(self, new_id):
        assert self.id == new_id