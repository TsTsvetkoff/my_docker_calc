import socket


HOST = 'server'

PORT = 5555
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (HOST, PORT)
HEADER = 64
FORMAT = 'utf-8'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    data = input("Enter two positive numbers (or '!DISCONNECT' to disconnect): ")
    if data == DISCONNECT_MESSAGE:
        client.send(data.encode(FORMAT))
        break
    else:
        client.send(data.encode(FORMAT))
        result = client.recv(HEADER).decode(FORMAT)
        print("Result: ", result)

client.close()
