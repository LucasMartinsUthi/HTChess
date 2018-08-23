import socket
import sys
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.229.7.116', 7005)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(2)
p1 = {}
p2 = {}
turno = 1
while True:
	connection, client_address = sock.accept()
	data = connection.recv(1024).decode()
	data = json.loads(data)
	if data['id'] == '1':
		p1 = data
		p2.update({'turno': turno})
		print(p2)
		arr = json.dumps(p2, ensure_ascii=False).encode('utf8')
		connection.send(arr)
	elif data['id'] == '2':
		p2 = data
		p1.update({'turno': turno})
		arr = json.dumps(p1, ensure_ascii=False).encode('utf8')
		connection.send(arr)
	elif data['id'] == '3':
		turno = turno%2 + 1
		arr = json.dumps({"funcionou": True}, ensure_ascii=False).encode('utf8')
		connection.send(arr)
connection.close()