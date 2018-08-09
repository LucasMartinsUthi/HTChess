import pygame
from random import randint

class classJogador:

	def __init__(self):
		self.canvas = pygame.display.set_mode([1000, 720])
		self.deck = [{'name': "queen",  'mana': 7, 'atack': 4, 'life': 6},
                    {'name': "knight", 'mana': 4, 'atack': 4, 'life': 3},
                    {'name': "knight", 'mana': 4, 'atack': 4, 'life': 3},
                    {'name': "bishop", 'mana': 3, 'atack': 0, 'life': 6},
                    {'name': "bishop", 'mana': 3, 'atack': 0, 'life': 6},
                    {'name': "rook", 'mana': 3, 'atack': 2, 'life': 6},
                    {'name': "rook", 'mana': 3, 'atack': 2, 'life': 6},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6}]
		self.mesa = {-3: {'ocupado': False, 'pos': [40, 300], 'rect': pygame.draw.rect(self.canvas, [0, 0, 0], ([40, 300],[100,180]))},
                   -2: {'ocupado': False, 'pos': [180, 300],'rect': pygame.draw.rect(self.canvas, [0, 0, 0], ([180, 300],[100,180]))},
                   -1: {'ocupado': False, 'pos': [320, 300],'rect': pygame.draw.rect(self.canvas, [0, 0, 0], ([320, 300],[100,180]))},
                    0: {'ocupado': False, 'pos': [460, 300],'rect': pygame.draw.rect(self.canvas, [0, 0, 0], ([460, 300],[100,180]))},
                    1: {'ocupado': False, 'pos': [600, 300],'rect': pygame.draw.rect(self.canvas, [0, 0, 0], ([600, 300],[100,180]))},
                    2: {'ocupado': False, 'pos': [740, 300],'rect': pygame.draw.rect(self.canvas, [0, 0, 0], ([740, 300],[100,180]))},
                    3: {'ocupado': False, 'pos': [880, 300],'rect': pygame.draw.rect(self.canvas, [0, 0, 0], ([880, 300],[100,180]))}}
		self.vida = 10
		self.mana = 1
		self.mao = []
		self.cartaSelecionada = None
		self.button = None
		self.debug = 10
		self.initDraw()
		self.geraDeck()

	def initDraw(self):
		self.canvas.fill([0, 0, 0])
		pygame.draw.rect(self.canvas, [130, 89, 9], ([0,500], [1280, 220]))
		self.button = pygame.draw.rect(self.canvas, [130, 130, 10], ([0,0], [100, 50]))


	def geraDeck(self):
		for i in reversed(range(0, len(self.deck))):
			randI = randint(0,14)
			randItem = self.deck[randI]

			self.deck[randI] = self.deck[i]
			self.deck[i] = randItem

	def selectCarta(self):
		pass

	def addMana(self):
		pass

	def addMao(self):
		if len(self.mao) == 7:
			print('Mão Cheia')
		else:
			self.mao.append({'carta': self.deck[0]})
			self.deck.pop(0)
			self.drawMao()

	def addCartaMesa(self, pos1 = 0, pos2 = 1):
		chaves = [key for key, val in self.mesa.items() if val['ocupado']]

		if not chaves:
			self.mesa[0]['ocupado'] = True
			self.mesa[0]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 255], (self.mesa[0]['pos'] ,[100,180]))
			return True

		menor = min(chaves)
		maior = max(chaves)

		if abs(menor) == 3:
			print('cheio')
			return False
		else:
			if abs(menor) == abs(maior):
				# pos2 +
				self.mesa[pos2]['ocupado'] = True
				self.mesa[pos2]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 255], (self.mesa[pos2]['pos'] ,[100,180]))
				i = pos2
				while i <= maior:
					self.mesa[i+1]['ocupado'] = True
					self.mesa[i+1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 255], (self.mesa[i+1]['pos'] ,[100,180]))
					i += 1
				return True
			else:
				# pos1 -
				self.mesa[pos1]['ocupado'] = True
				self.mesa[pos1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 255], (self.mesa[pos1]['pos'] ,[100,180]))
				i = pos1
				while i >= menor:
					self.mesa[i-1]['ocupado'] = True
					self.mesa[i-1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 255], (self.mesa[i-1]['pos'] ,[100,180]))
					i -= 1
				return True

		return True

	def drawMao(self):
		pos = [40, 520]
		i = 0
		for carta in self.mao:
			if i == self.cartaSelecionada:
				pos[0] += 140
				i += 1
				continue				
			self.mao[i].update({'rect': pygame.draw.rect(self.canvas, [0, 50, 255], (pos,[100,180]))})
			pos[0] += 140
			i += 1

		return True

	def drawMesa(self):
		for casa in self.mesa:
			if self.mesa[casa]['ocupado'] == True:
				self.mesa[casa]['rect']	= pygame.draw.rect(self.canvas, [0, 0, 255], (self.mesa[casa]['pos'] ,[100,180]))

		return True

	def drawDrag(self):
		i = 0
		pos = [pygame.mouse.get_pos()[0]-50, pygame.mouse.get_pos()[1] - 90]
		for carta in self.mao:
			if i == self.cartaSelecionada:				
				self.mao[i].update({'rect': pygame.draw.rect(self.canvas, [0, 50, 255], (pos, [100,180]))})
			i += 1

		return True

	def drawTabuleiro(self):
		pass

	def drawAdversario(self):
		pass


		
