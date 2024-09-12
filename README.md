# Python Socket Programming with Docker

This project demonstrates how to use Python's socket programming capabilities to create a server-client architecture, where the server can handle multiple clients. The server and clients are each run in their own Docker containers.
The server is a simple calculator that can perform addition operations of two positive numbers. 
The clients can connect to the server and send requests to perform these operations.

## Project Structure

- `server/`: This directory contains the server code and its Dockerfile.
- `client/`: This directory contains the client code and its Dockerfile.
- `docker-compose.yaml`: This file is used to define and run the multi-container Docker application.

## Prerequisites
- Docker
## How to Run

1. Build and start the Docker containers:

```bash
docker-compose build
docker-compose up
```
2. Open a new terminal window and review the newly created active containers:
```bash
docker ps -a
```
Focus on the following CT names:
```bash
NAMES
my_docker_calc-client1-1
my_docker_calc-client2-1
my_docker_calc-server-1
```
3. In this terminal attach to the client 1 container:
```bash
docker attach my_docker_calc-client1-1
```

4. You can utilize the client 2 in another terminal window by running:
```bash
docker attach my_docker_calc-client2-1
```

Enjoy the server-client communication!