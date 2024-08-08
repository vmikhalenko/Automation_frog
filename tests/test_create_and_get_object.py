import pytest

@pytest.mark.smoke
def test_get_one_object(create_object, object_getter_endp):
    id, body = create_object
    object_getter_endp.get_one_obj_by_id(id)
    object_getter_endp.check_response_status_is_ok()
    object_getter_endp.check_id_same_as_sent(id)