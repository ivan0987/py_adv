import json
import yaml
import socket
import argparse
import logging
from server.actions import (resolve, get_server_actions)
from server.protocol import (validate_request, make_response, make_400, make_404)
from server.settings import (HOST, PORT, BUFFERSIZE, ENCODING)

'''Принты я тоже оставил - мне так удобнее'''

host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODING

log = logging.getLogger('server')

parser = argparse.ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration'
)
args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        conf = yaml.load(file, Loader=yaml.Loader)
        host = conf.get('host', HOST)
        port = conf.get('port', PORT)
        buffersize = conf.get('buffersize', BUFFERSIZE)
        encoding = conf.get('encoding', ENCODING)

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(10)
    server_actions = get_server_actions()

    print('Server started')
    log.info('Server started')

    while True:
        client, address = sock.accept()
        print(f'Client with address { address } was detected')
        log.info(f'Client with address { address } was detected')

        b_request = client.recv(buffersize)
        request = json.loads(b_request.decode(encoding))

        action_name = request.get('action')

        if validate_request(request):
            controller = resolve(action_name, server_actions)
            if controller:
                try:
                    response = controller(request)
                except Exception as err:
                    print(err)
                    log.critical(err)
                    response = make_response(
                        request, 500, 'Internal server error'
                    )
            else:
                print(f'Action with name { action_name } does not exists')
                log.error(f'Action with name { action_name } does not exists')
                response = make_404(request)
        else:
            print(f'Request is not valid')
            log.error('Request is not valid')
            response = make_400(request)

        s_response = json.dumps(response)
        client.send(s_response.encode(encoding))

        client.close()
except KeyboardInterrupt:
    print('Client closed')
    log.info('Client closed')
