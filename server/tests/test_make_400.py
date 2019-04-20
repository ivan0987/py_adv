from server.protocol import make_400, make_response


def test_make_400():
    request = {
        'action': None,
        'user': None,
        'time': None,
        'data': None,
        'code': None
    }

    expected = {
        'action': None,
        'user': None,
        'time': None,
        'data': 'Wrong request format',
        'code': 400
    }

    assert make_400(request).get('data') == expected.get('data')