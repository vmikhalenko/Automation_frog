import requests
from endpoints.endpoints_handler import Endpoint

class PatchObjectEndpoint(Endpoint):
    def update_part_of_object(self,body):
        response = requests.patch(
            'https://api.restful-api.dev/objects/ff808181910cdad101910d9f04c902d6',
            headers={'Content-Type': 'application/json'},
            json=body
        )
        self.status = response.status_code
        self.id = response.json()['id']
        self.name = response.json()['name']
        self.updateAt = response.json()['updatedAt']
        print(response.json())
        return response.json()['id']

    def check_id_param_is_not_null(self):
        assert self.id is not None

    def check_name_same_as_sent(self):
        assert self.name == 'Huawei 20 (Updated Name)'

    def check_updated_param_is_not_null(self):
        assert self.updateAt is not None