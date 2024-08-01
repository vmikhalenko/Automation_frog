import pytest
from endpoints.create_object_endpoint import CreateObjectEndpoint
from endpoints.get_object_endpoint import GetObjectEndpoint
from endpoints.put_object_endpoint import PutObjectEndpoint
from endpoints.patch_object_endpoint import PatchObjectEndpoint
from endpoints.delete_object_endpoint import DeleteObjectEndpoint

@pytest.fixture()
def object_creator_endp():
    return CreateObjectEndpoint()

@pytest.fixture()
def object_getter_endp():
    return GetObjectEndpoint()

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

@pytest.fixture()
def object_update_endp():
    return PutObjectEndpoint()

@pytest.fixture()
def object_part_update_endp():
    return PatchObjectEndpoint()

@pytest.fixture()
def object_delete_endp():
    return DeleteObjectEndpoint()