import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.228.254.181', 4000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)
while True:
    # Find connections
    connection, client_address = sock.accept()
    try:
        data = connection.recv(1024)
        print (data.decode())
    except:
        connection.close()