import socket

client_socket = socket.socket()

client_socket.connect(('localhost', 4001))

msg = client_socket.recv(1024)
while msg:
    print(msg.decode())
    msg = client_socket.recv(1024)

client_socket.close()