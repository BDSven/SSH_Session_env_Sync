#!/usr/bin/python
# Environment Var server, waiting for input and providing vars to client.
# Running always in the background and listening to the defined socket 
# All variables to be configured at at the top from the main block
# This script needs to be called using: `env_server.py &`

import json
import socket
import os
from pprint import pprint

def read_all_env_vars():
    return os.environ.items()

def return_selected_env_vars():
    global env_vars_to_export
    env_vars = read_all_env_vars()
    selected_vars= {}
    for key, value in env_vars:
        if key in env_vars_to_export:
            selected_vars[key] = value
    return selected_vars

def socket_wait_for_connection():   
    conn, _ = server.accept()
    with conn:
        answer_connection(conn)

def answer_connection(conn):
    data = conn.recv(1024)
    if data:
        check_and_answer_cmd(data,conn)       

def  check_and_answer_cmd(data,conn):
    data_encoded = data.decode()
    try:
        data_json = json.loads(data_encoded)
    except Exception as error :
        print (f"ENV-SERVER: {error} ")

    if "getenv" in data_json['cmd']:                                       
        conn.sendall( json.dumps(return_selected_env_vars()).encode() )
	


if __name__ == "__main__":

    env_vars_to_export = ['SSHPASS', 'VAR1', 'VAR2', 'VARn']
    SOCKET_PATH = "/tmp/env_sync.socket"

    data_json= {}
  
    if os.path.exists(SOCKET_PATH):
        os.remove(SOCKET_PATH)

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(SOCKET_PATH)
        server.listen(1)
        print("Environment Server started.")

        while True:
            socket_wait_for_connection()


