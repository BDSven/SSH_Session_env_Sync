# Explanation

This script works only on a single unix box.
I don't intend to use it over multiple linux boxes, so there will be no TCP extension for this.

Before using it the first time, you need to adjust the following variables in env_server.py
- env_vars_to_export
- SOCKET_PATH
And the following variables in env_client.py
- SOCKET_PATH
Maybe I'm going to create a common variable file in the future, which will make this step easier.

Make sure to use a secure path for the Socket File, ie. your home folder.

The scripts are provided as is, without any warranty!
To avoid any damage, don't use them in a productive environment.

# Starting Server

The server can be started on your first SSH Session.
If will wait for a connected client and answer the request for the environment.
The server is running as long as the first SSH Session is established.

At best it should be started using `env_server.py &`.

# Starting the client

The client can be automatically started, whenever you open an SSH Session to the server.
Once it is started, it connects to the server, received the environment variablesand prints the export Commands.

For example you can add it to your local `.bashrc` file with the following line: 
```bash
source <(python3 env_client.py)
```
