from server.protocol import validate_request


def test_validate_request():
    request = {
        'action': 'action',
        'user': None,
        'time': 'time',
        'data': None,
        'code': None
    }

    expected = True

    assert validate_request(request) == expected
