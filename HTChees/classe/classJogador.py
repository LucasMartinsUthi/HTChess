from random import randint

class classJogador:

	def __init__(self):
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
		self.geraDeck()
		pass

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
		self.mao.append(self.deck[0])
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

	def update(self):
		pass
		