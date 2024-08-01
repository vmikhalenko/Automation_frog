import requests
from endpoints.endpoints_handler import Endpoint

class DeleteObjectEndpoint(Endpoint):
    def delete_object(self):
        response = requests.delete(
            'https://api.restful-api.dev/objects/ff808181910cdad101910d9ec38e02d5'
        )
        self.status = response.status_code
        self.message = response.json()['message']
        print(response.json())
        return response.json()['message']


    def check_id_in_message_same_as_sent(self, id):
        expected_message = f'Object with id = {id} has been deleted.'
        assert self.message == expected_message, f"Expected message: '{expected_message}', but got: '{self.message}'"