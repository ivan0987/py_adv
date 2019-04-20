from server.protocol import make_404, make_response


def test_make_404():
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
        'data': 'Action is not supported',
        'code': 404
    }

    assert make_404(request).get('data') == expected.get('data')