import socket
import json

while True:
	clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	clientsocket.connect(('10.228.254.181', 4000))
	msn = input('Mensagem: ')
	arr = json.dumps([msn, {'nome': 'Peão', 'atk': 1, 'vida': 6}], ensure_ascii=False).encode('utf8')
	clientsocket.send(arr)