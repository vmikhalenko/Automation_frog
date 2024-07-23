import pytest
from endpoints.Create_Url_Endpoint import CreateUrlEndpoint
from endpoints.Get_Url_Endpoint import GetUrlEndpoint

@pytest.fixture()
def object_creator_endp():
    return CreateUrlEndpoint()

@pytest.fixture()
def url_getter_endp():
    return GetUrlEndpoint()

@pytest.fixture()
def create_object(object_creator_endp):
    body = {
            "name": "Apple MacBook Pro 20",
            "data": {
                "year": 2024,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
    object_creator_endp.add_new_object(body)
    return object_creator_endp.id, body

