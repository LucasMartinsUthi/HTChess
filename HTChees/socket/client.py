import pygame
import sys
import copy
import socket
import json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

id  = input('Qual jogador vc é: ')

con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
con.connect(('10.228.254.181', 7013))

while True:
	msn = input("Mensagem: ")
	arr = json.dumps({'id': id ,  'msn': msn}, ensure_ascii=False).encode('utf8')
	con.send(arr)
	resposta = con.recv(1024).decode()
