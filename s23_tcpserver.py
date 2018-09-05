import socket

host = 'localhost'
port = 4001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

server_socket.listen(1)

cnnct,addr = server_socket.accept()


print("Hello, {}".format(str(addr)))


cnnct.send(b'Hello!, How are you?')
cnnct.send("bye".encode())
cnnct.close()

