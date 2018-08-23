import socket
import sys
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 7016)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(2)
p1 = {}
p2 = {}
while True:
    # Find connections
	connection, client_address = sock.accept()
	data = connection.recv(1024).decode()
	data = json.loads(data)
	if data['id'] == '1':
		p1 = data
		arr = json.dumps(p2, ensure_ascii=False).encode('utf8')
		connection.send(arr)
	else:
		p2 = data
		arr = json.dumps(p1, ensure_ascii=False).encode('utf8')
		connection.send(arr)
connection.close()