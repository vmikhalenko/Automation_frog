def test_add_object(object_creator_endp):
    # test data
    body = {
            "name": "HP pro 18",
            "data": {
                "year": 2023,
                "price": 1499.99,
                "CPU model": "Intel Core i7",
                "Hard disk size": "1 TB"
            }
        }
    object_creator_endp.add_new_object(body)
    object_creator_endp.check_response_status_is_ok()
    object_creator_endp.check_id_param_is_not_null()
    object_creator_endp.check_name_same_as_sent()