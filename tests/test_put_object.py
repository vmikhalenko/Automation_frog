def test_put_object(object_update_endp):
    # test data
    body = {
            "name": "Samsung pro 18",
            "data": {
                "year": 2021,
                "price": 1300.99,
                "CPU model": "Intel Core i7",
                "Hard disk size": "1 TB"
            }
        }
    object_update_endp.update_object(body)
    object_update_endp.check_id_param_is_not_null()
    object_update_endp.check_response_status_is_ok()
    object_update_endp.check_name_same_as_sent()