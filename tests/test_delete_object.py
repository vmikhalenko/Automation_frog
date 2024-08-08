import pytest

@pytest.mark.regression
def test_delete_object(object_delete_endp):
    object_delete_endp.delete_object()
    object_delete_endp.check_response_status_is_ok()
    object_delete_endp.check_id_in_message_same_as_sent('ff808181910cdad101910d9ec38e02d5')