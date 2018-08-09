import pygame
from random import randint

class classJogador:

	def __init__(self):
		self.canvas = pygame.display.set_mode([1280, 720])
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
		self.mesa = {-3: {'ocupado': False},
                   -2: {'ocupado': False}, 
                   -1: {'ocupado': False}, 
                    0: {'ocupado': False},
                    1: {'ocupado': False}, 
                    2: {'ocupado': False}, 
                    3: {'ocupado': False}}
		self.vida = 10
		self.mana = 1
		self.mao = []
		self.cartaSelecionada = []
		self.button = None
		self.debug = 10
		self.initDraw()
		self.geraDeck()

	def initDraw(self):
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
			self.mao.append({'carta': self.deck[0], 'rect': self.drawMao()})
			self.deck.pop(0)

	def addCartaMesa(self):
		chaves = [key for key, val in self.mesa.items() if val['ocupado']]

		if not chaves:
			mesa[0]['ocupado'] = True
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
				i = pos2
				while i <= maior:
					self.mesa[i + 1] = self.mesa[i]
					i += 1
				return True
			else:
				# pos1 -
				self.mesa[pos1]['ocupado'] = True
				i = pos1
				while i >= menor:
					self.mesa[i - 1] = self.mesa[i]
					i -= 1
				return True

		return True

	def drawMao(self):
		print(len(self.mao))
		pos = [40, 520]
		for carta in self.mao:
			pos[0] += 140

		return pygame.draw.rect(self.canvas, [0, 50, 255], (pos,[100,180]))

	def drawTabuleiro(self):
		pass

	def drawAdversario(self):
		pass


		