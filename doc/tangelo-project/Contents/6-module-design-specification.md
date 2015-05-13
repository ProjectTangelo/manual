#Module Description#

## User console

This is the key part of the product. This is what allows the user to interact with their Linux container instance. It is served on a different server and presents live updates of STDOUT to the user. It is done with WebSockets and is encrypted. It has methods to authenticate and verify user sessions so that each user will be able to access their container instance without interferring with another user.

## User interaction scripts

There are interaction scripts that are in each container that allow the user to upload their work from their instance to the server so that it can be reviewed later. The use case for this for example could be a student uploading their homework for an administrator to grade. 

## Web UI

The product is meant to be used from the browser. The front-end is served from a Node.JS server running on the master node and provides session handling and management for the administrator and user. The administrator will be able to upload documents and mangage instances. The user will be able to use the console to access their Linux instances.

## Salt Modules

Salt modules are programs that are invoked by Salt to provide communication and RPC from a master server to minions. We current use this to get information about the servers such as free memory, CPU usage and setting quotas for containers. 