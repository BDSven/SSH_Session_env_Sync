#!/usr/bin/python
# This script needs to be called using: source <(python3 env_client.py)
#Env. Client, started after logon and setting vars defined at server.

import socket
import json
from pprint import pprint

SOCKET_PATH = "/tmp/env_sync.socket"

def print_export_vars(data_vars):
    for key, value in data_vars.items():
        print (f"export {key}='{value}'")
    print('echo -e "\033[0;32m OK:\033[0m DEV Environment copied from Server!"' )
    pass

if __name__ == "__main__":

    data = False

    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
            client.connect(SOCKET_PATH)
            client.sendall(b'{"cmd": "getenv"}')
            data = client.recv(1024).decode()
    except Exception as error:
        print('echo -e "\033[0;31m ERROR:\033[0m ENVIRONMENT SERVER IS NOT RUNNING !"' )

    if data :
        data_dict = json.loads(data)
        print_export_vars(data_dict)

