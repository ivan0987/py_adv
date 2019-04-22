from datetime import datetime
from server.protocol import make_response


def test_make_response():
    request = {
        'action': 'test',
        'user': 'test_user',
        'time': datetime.now().timestamp(),
        'data': 'test_data',
        'code': 'test_code'
    }

    expected = {
        'action': 'test',
        'user': 'test_user',
        'time': datetime.now().timestamp(),
        'data': None,
        'code': 200
    }

    assert make_response(request, 200) == expected
