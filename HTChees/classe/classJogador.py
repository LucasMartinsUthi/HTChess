import pygame
from random import randint
import copy
import socket
import json
# from signal import signal, SIGPIPE, SIG_DFL

# signal(SIGPIPE, SIG_DFL)

class classJogador:

	def __init__(self):
		self.width = 1280
		self.height = 720
		self.canvas = pygame.display.set_mode([self.width, self.height])
		pygame.font.init()
		self.font = pygame.font.SysFont('Helvetica', 20)
		self.id = None
		self.deck = [{'name': "queen",  'mana': 7, 'atack': 4, 'life': 6, 'cor': [0, 0, 255]},
                    {'name': "knight", 'mana': 4, 'atack': 4, 'life': 3, 'cor': [0, 255, 0]},
                    {'name': "knight", 'mana': 4, 'atack': 4, 'life': 3, 'cor': [0, 255, 0]},
                    {'name': "bishop", 'mana': 3, 'atack': 0, 'life': 6, 'cor': [255, 0, 0]},
                    {'name': "bishop", 'mana': 3, 'atack': 0, 'life': 6, 'cor': [255, 0, 0]},
                    {'name': "rook", 'mana': 3, 'atack': 2, 'life': 6, 'cor': [255, 255, 0]},
                    {'name': "rook", 'mana': 3, 'atack': 2, 'life': 6, 'cor': [255, 255, 0]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'cor': [255, 0, 255]}]
		self.mesa = {-3: {'ocupado': False, 'pos': [70, self.height/2 + 30], 'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([70, self.height/2 + 30],[140,150]))},
                   -2: {'ocupado': False, 'pos': [210, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([210, self.height/2 + 30],[140,150]))},
                   -1: {'ocupado': False, 'pos': [350, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([350, self.height/2 + 30],[140,150]))},
                    0: {'ocupado': False, 'pos': [490, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([490, self.height/2 + 30],[140,150]))},
                    1: {'ocupado': False, 'pos': [630, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([630, self.height/2 + 30],[140,150]))},
                    2: {'ocupado': False, 'pos': [770, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([770, self.height/2 + 30],[140,150]))},
                    3: {'ocupado': False, 'pos': [910, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([910, self.height/2 + 30],[140,150]))}}
		self.vida = 20
		self.manaTotal = 0
		self.mana = 0
		self.mao = []
		self.cartaSelecionada = None
		self.button = None
		self.debug = 10
		self.bkpMesa  = copy.deepcopy(self.mesa)
		self.inimigo = None
		self.con = True
		self.initDraw()
		self.geraDeck()

	def initDraw(self):
		self.canvas.fill([0, 0, 0])

		mesa = pygame.draw.rect(self.canvas, [130, 89, 9], ([0,540], [1280, 180]))
		textsurface = self.font.render(str(self.vida) + " - " + str(self.mana) + "/" + str(self.manaTotal), False, (0, 0, 0))
		self.canvas.blit(textsurface, [1200, self.height-170])

		inimigo = pygame.draw.rect(self.canvas, [130, 89, 9], ([0,0], [1280, 180]))
		if self.inimigo != None and list(self.inimigo.keys()) != ['turno'] :
			textsurface = self.font.render(str(self.inimigo['vida']) + " - " + str(self.inimigo['manaTotal']) + "/" + str(self.inimigo['manaTotal']), False, (0, 0, 0))
			self.canvas.blit(textsurface, [1200, 10])
		else:
			textsurface = self.font.render("Procurando por Inimigos", False, (0, 0, 0))
			self.canvas.blit(textsurface, [self.width/2 - 120, 10])

		self.button = pygame.draw.rect(self.canvas, [130, 130, 10], ([self.width - 100, self.height/2 -25], [100, 50]))
		textsurface = self.font.render('Turno', False, (0, 0, 0))
		self.canvas.blit(textsurface, self.button)

	def socket(self, turno = False):
		con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		con.connect(('10.229.7.116', 7003))
		if turno:
			arr = json.dumps({'id': '3'}, ensure_ascii=False).encode('utf8')
			con.send(arr)
			return True

		mesa = {}
		chavesMesa = [key for key, val in self.mesa.items()]
		for chave in chavesMesa:
			mesa.update({chave : self.mesa[chave]['ocupado']})
		arr = json.dumps({'id': self.id, 'lenMao' : len(self.mao), 'mesa' : mesa, 'lenDeck': len(self.deck), 'vida': self.vida, 'mana': self.mana, 'manaTotal': self.manaTotal}, ensure_ascii=False).encode('utf8')
		con.send(arr)
		resposta = con.recv(1024).decode()
		resposta = json.loads(resposta)
		self.inimigo = resposta
		self.con = True
		return True

	def geraDeck(self):
		for i in reversed(range(0, len(self.deck))):
			randI = randint(0,14)
			randItem = self.deck[randI]

			self.deck[randI] = self.deck[i]
			self.deck[i] = randItem
		
	def addMao(self):
		if len(self.mao) == 10:
			print('Mão Cheia')
		else:
			self.mao.append({'carta': self.deck[0]})
			self.deck.pop(0)
		return self.mao

	def addCartaMesa(self, pos):
		if self.mana - int(self.mao[self.cartaSelecionada]['carta']['mana']) < 0:
			print("Mana Insuficiente")
			return True
		else:
			 self.mana -= int(self.mao[self.cartaSelecionada]['carta']['mana'])

		ocupado = copy.deepcopy(self.mao[self.cartaSelecionada]['carta'])
		chaves = [key for key, val in self.mesa.items() if val['ocupado']]
		if not chaves:
			self.mesa[0]['ocupado'] = ocupado
			self.mesa[0]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[0]['pos'] ,[100,150]))
			self.mao.pop(self.cartaSelecionada)
			return True

		menor = min(chaves)
		maior = max(chaves)

		if abs(menor) == 3:
			print('cheio')
			return False
		else:
			if abs(menor) == abs(maior):
				if pos <= menor:
					i = maior
					while i >= menor:
						self.mesa[i+1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i+1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i -= 1
					pos = menor
				elif menor < pos <= maior:
					i = maior
					while i >= pos:
						self.mesa[i+1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i+1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i -= 1
				elif pos > maior:
					pos = maior + 1
			else:
				# pos1 -
				if pos >= maior:
					i = menor
					while i <= maior:
						self.mesa[i-1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i-1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i-1]['pos'] ,[100,150]))
						i += 1
					pos = maior
				elif menor <= pos < maior:
					i = menor
					while i <= pos:
						self.mesa[i-1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i-1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i += 1
				elif pos < menor:
					pos = menor - 1

			self.mesa[pos]['ocupado'] = ocupado
			self.mesa[pos]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[pos]['pos'] ,[100,150]))
		
		self.mao.pop(self.cartaSelecionada)
		return True

	def previewCartaMesa(self, pos):
		ocupado = True
		self.bkpMesa = copy.deepcopy(self.mesa)
		chaves = [key for key, val in self.mesa.items() if val['ocupado']]
		if not chaves:
			self.mesa[0]['ocupado'] = ocupado
			self.mesa[0]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[0]['pos'] ,[100,150]))
			self.drawMesa(True)
			return True

		menor = min(chaves)
		maior = max(chaves)

		if abs(menor) == 3:
			print('cheio')
			self.drawMesa(True)
			return False
		else:
			if abs(menor) == abs(maior):
				if pos <= menor:
					i = maior
					while i >= menor:
						self.mesa[i+1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i+1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i -= 1
					pos = menor
				elif menor < pos <= maior:
					i = maior
					while i >= pos:
						self.mesa[i+1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i+1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i -= 1
				elif pos > maior:
					pos = maior + 1
			else:
				# pos1 -
				if pos >= maior:
					i = menor
					while i <= maior:
						self.mesa[i-1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i-1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i-1]['pos'] ,[100,150]))
						i += 1
					pos = maior
				elif menor <= pos < maior:
					i = menor
					while i <= pos:
						self.mesa[i-1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i-1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i += 1
				elif pos < menor:
					pos = menor - 1

			self.mesa[pos]['ocupado'] = ocupado
			self.mesa[pos]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[pos]['pos'] ,[100,150]))
		
		self.drawMesa(True)
		return True

	def drawMao(self):
		pos = [20, 564]
		i = 0
		for carta in self.mao:
			if i == self.cartaSelecionada:
				pos[0] += 104
				i += 1
				continue				
			self.mao[i].update({'rect': pygame.draw.rect(self.canvas, carta['carta']['cor'], (pos,[100,180]))})
			atackVida = self.font.render(str(self.mao[i]['carta']['atack']) + "/" + str(self.mao[i]['carta']['life']) + "  -- " + str(self.mao[i]['carta']['mana']), False, (0, 0, 0))
			self.canvas.blit(atackVida, self.mao[i]['rect'])
			pos[0] += 120
			i += 1

		return True

	def drawMesa(self, preview = False):
		lenChaves = len([key for key, val in self.mesa.items() if val['ocupado']])
		ajuste = 0
		if lenChaves % 2 == 0 and lenChaves != 0:
			ajuste  = -70
		chaves = list(self.mesa.keys())
		chaves.sort()

		for casa in chaves:
			pos = list(self.mesa[casa]['pos'])
			pos[0] += ajuste
			if self.mesa[casa]['ocupado'] != False and self.mesa[casa]['ocupado'] != True:
				atack = self.mesa[casa]['ocupado']['atack']
				atack = str(atack)
				vida = self.mesa[casa]['ocupado']['life']
				vida = str(vida)
				mana = self.mesa[casa]['ocupado']['mana']
				mana = str(mana)
				self.mesa[casa]['rect']	= pygame.draw.rect(self.canvas, self.mesa[casa]['ocupado']['cor'], (pos ,[100,100]))
				atackVida = self.font.render(atack + "/" + vida + " -- " + mana, False, (0, 0, 0))
				self.canvas.blit(atackVida, self.mesa[casa]['rect'])
			elif self.mesa[casa]['ocupado'] == True:
				self.mesa[casa]['rect']	= pygame.draw.rect(self.canvas, [155, 155, 155], (pos ,[100,100]), 1)
			else:
				self.mesa[casa]['rect']	= pygame.draw.rect(self.canvas, [0, 0, 0], (pos ,[100,150]), 1)
		if preview:
			self.mesa = copy.deepcopy(self.bkpMesa)
		return True

	def drawDrag(self):
		i = 0
		pos = [pygame.mouse.get_pos()[0]-50, pygame.mouse.get_pos()[1] - 90]
		for carta in self.mao:
			if i == self.cartaSelecionada:				
				self.mao[i].update({'rect': pygame.draw.rect(self.canvas, carta['carta']['cor'], (pos, [100,180]))})
				atackVida = self.font.render(str(carta['carta']['atack']) + "/" + str(carta['carta']['life']) + "  -- " + str(carta['carta']['mana']), False, (0, 0, 0))
				self.canvas.blit(atackVida, self.mao[i]['rect'])
			i += 1

		return True

	def drawInimigo(self):
		if self.con:
			self.con = False
			self.socket()

		if self.inimigo != None and list(self.inimigo.keys()) != ['turno']:
			mao = self.inimigo['lenMao']
			pos = [20, -24]
			for i in range(mao):
				pygame.draw.rect(self.canvas, (158, 100, 0), (pos,[100,180]))
				pos[0] += 120

			mesa = {}
			for carta in self.inimigo['mesa'].items():
				mesa.update({carta[0]: carta[1]})

			lenChaves = len([key for key, val in mesa.items() if val])
			ajuste = 0
			if lenChaves % 2 == 0 and lenChaves != 0:
				ajuste  = -70
			chaves = list(mesa.keys())
			chaves.sort()
			for casa in chaves:
				pos = (copy.deepcopy(self.mesa[int(casa)]['pos']))
				pos[0] += ajuste
				pos[1] -= 160
				if mesa[casa] != False:
					cartaInimigo = pygame.draw.rect(self.canvas, mesa[casa]['cor'], (pos ,[100,100]))
					atackVida = self.font.render(str(mesa[casa]['atack']) + "/" + str(mesa[casa]['life']) + "  -- " + str(mesa[casa]['mana']), False, (0, 0, 0))
					self.canvas.blit(atackVida, cartaInimigo)

				else:
					pygame.draw.rect(self.canvas, [0, 0, 0], (pos ,[100,150]), 1)
		else:
			print('Nenhum Inimigo Encontrado')

		return True

	def defesaInimigo(self):
		try:
			self.inimigo['mesa']
		except:
			return True
		inimigo = self.inimigo['mesa']
		mesa = self.mesa
		lenInimigo = len([key for key, val in inimigo.items() if val])
		lenMesa = len([key for key, val in mesa.items() if val['ocupado']])
		print(lenInimigo, inimigo, "\n")
		print(lenMesa, mesa, "\n")
		for i in range(-3, 3):
			if (lenInimigo - lenMesa) % 2 == 0:
				if inimigo[str(i)] != False:
					if mesa[i]['ocupado'] != False:
						mesa[i]['ocupado']['life'] = mesa[i]['ocupado']['life'] - inimigo[str(i)]['atack']
						if mesa[i]['ocupado']['life'] <= 0:
							mesa[i]['ocupado'] = False
					else:
						pass #bate cara
			else:
				if inimigo[str(i)] != False:
					if mesa[i]['ocupado'] != False:
						mesa[i]['ocupado']['life'] = mesa[i]['ocupado']['life'] - inimigo[str(i)]['atack']
						mesa[i-1]['ocupado']['life'] = mesa[i-1]['ocupado']['life'] - inimigo[str(i)]['atack']
						if mesa[i]['ocupado']['life'] <= 0:
							mesa[i]['ocupado'] = False
						if mesa[i-1]['ocupado']['life'] <= 0:
							mesa[i-1]['ocupado'] = False
					else:
						pass #bate cara
		return True

	def addMana(self):
		self.manaTotal += 1
		self.mana = int(self.manaTotal)
