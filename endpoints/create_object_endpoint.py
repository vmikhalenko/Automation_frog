# creating framework

import requests
from endpoints.endpoints_handler import Endpoint


class CreateObjectEndpoint(Endpoint):
    def add_new_object(self, body):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            json=body,
            headers={'Content-Type': 'application/json'}
        )
        self.status = response.status_code
        self.id = response.json()['id']
        self.name = response.json()['name']
        print(response.json())
        return response.json()['id']

    def check_id_param_is_not_null(self):
        assert self.id is not None

    def check_name_same_as_sent(self):
        assert self.name == 'HP pro 18'

