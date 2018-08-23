from graphics import *
from random import randint

class classJogo(object):


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
        self.tab = {-3: {'ocupado': False},
                   -2: {'ocupado': False}, 
                   -1: {'ocupado': False}, 
                    0: {'ocupado': False},
                    1: {'ocupado': False}, 
                    2: {'ocupado': False}, 
                    3: {'ocupado': False}}
        self.geraDeck()

    def geraDeck(self):
        for i in reversed(range(0, len(self.deck))):
            randI = randint(0,14)
            randItem = self.deck[randI]

            self.deck[randI] = self.deck[i]
            self.deck[i] = randItem

    def geraDeck(self):
        for i in reversed(range(0, len(self.deck))):
            randI = randint(0,14)
            randItem = self.deck[randI]

            self.deck[randI] = self.deck[i]
            self.deck[i] = randItem
        
    def addMao(self):
        if len(self.mao) == 7:
            print('Mão Cheia')
        else:
            self.mao.append({'carta': self.deck[0]})
            self.deck.pop(0)
            self.drawMao()

    def inserirPosicao(self, pos1, pos2):
        chaves = [key for key, val in self.tab.items() if val['ocupado']]

        if not chaves:
            tab[0]['ocupado'] = True
            return True

        menor = min(chaves)
        maior = max(chaves)

        if abs(menor) == 3:
            print('cheio')
            return False
        else:
            if abs(menor) == abs(maior):
                # pos2 +
                self.tab[pos2]['ocupado'] = True
                i = pos2
                while i <= maior:
                    self.tab[i + 1] = self.tab[i]
                    i += 1
                return True
            else:
                # pos1 -
                self.tab[pos1]['ocupado'] = True
                i = pos1
                while i >= menor:
                    self.tab[i - 1] = self.tab[i]
                    i -= 1
                return True

        return True

# def inserir():
#     chaves = [key for key, val in tab.items() if val['ocupado']]
#     if not chaves:
#         tab[0]['ocupado'] = True
#         return True
#     menor = min(chaves)
#     maior = max(chaves)

#     if abs(menor) == 3:
#         print('cheio')
#         return False
#     else:
#         if abs(menor) == abs(maior):
#             tab[maior + 1]['ocupado'] = True
#         else:
#             tab[menor - 1]['ocupado'] = True

#     return True

jogo = classJogo()

win = GraphWin("My Circle", 100, 100)
c = Circle(Point(50,50), 10)
c.draw(win)
win.getMouse()
win.close()

while True:
