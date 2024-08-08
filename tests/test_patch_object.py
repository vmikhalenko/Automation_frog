import pytest

@pytest.mark.regression
def test_update_part_of_object(object_part_update_endp):
    # test data
    body = {
            "name": "Huawei 20 (Updated Name)"
            }
    object_part_update_endp.update_part_of_object(body)
    object_part_update_endp.check_id_param_is_not_null()
    object_part_update_endp.check_response_status_is_ok()
    object_part_update_endp.check_name_same_as_sent()
    object_part_update_endp.check_updated_param_is_not_null()