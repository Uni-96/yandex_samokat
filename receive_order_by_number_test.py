import sender_stand_request

def test_receive_order_by_number_get_success_response():
    assert sender_stand_request.get_order_by_number.status_code == 200