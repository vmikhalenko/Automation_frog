def test_get_one_object(create_object, url_getter_endp):
    id, body = create_object
    url_getter_endp.get_one_obj_by_id(id)
    url_getter_endp.check_response_status_is_ok()
    url_getter_endp.check_id_same_as_sent(id)