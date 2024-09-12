import os
import socket
import threading
import logging

logging.basicConfig(level=logging.INFO)

HEADER = 64
# HOST = 'localhost'
container_id = os.environ.get('HOSTNAME')
HOST = socket.gethostbyname(container_id)
PORT = 5555
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (HOST, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    logging.info(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        data = conn.recv(HEADER).decode(FORMAT)
        if data == DISCONNECT_MESSAGE:
            connected = False
            logging.info(f"[DISCONNECT] {addr} disconnected.")
        else:
            try:
                num1, num2 = map(int, data.split())
                if num1 < 0 or num2 < 0:
                    conn.send("Received invalid numbers. Please send two positive integers.".encode(FORMAT))
                else:
                    res = num1 + num2
                    if res > 100:
                        conn.send("Result is greater than 100".encode(FORMAT))
                    else:
                        conn.send(str(res).encode(FORMAT))
            except ValueError:
                conn.send("Received invalid numbers. Please send two positive integers.".encode(FORMAT))

        logging.info(f"Msg received: [{addr}]: {data}")
    conn.close()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        logging.info(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


logging.info("[STARTING] server is starting...")
start()
