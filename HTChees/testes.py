from random import randint

class classJogo(object):
    deck = []

    def __init__(self):
        self.deck
        self.geraDeck()

    def geraDeck(self):
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

        for i in reversed(range(0, len(self.deck))):
            randI = randint(0,14)
            randItem = deck[randI]

            self.deck[randI] = self.deck[i]
            self.deck[i] = randItem

def inserir():
    chaves = [key for key, val in tab.items() if val['ocupado']]
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
            tab[maior + 1]['ocupado'] = True
        else:
            tab[menor - 1]['ocupado'] = True

    return True


def inserirPosicao(pos1, pos2):
    chaves = [key for key, val in tab.items() if val['ocupado']]

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
            tab[pos2]['ocupado'] = True
            i = pos2
            while i <= maior:
                tab[i + 1] = tab[i]
                i += 1
            return True
        else:
            # pos1 -
            tab[pos1]['ocupado'] = True
            i = pos1
            while i >= menor:
                tab[i - 1] = tab[i]
                i -= 1
            return True

    return True

tab = {-3: {'ocupado': False}, -2: {'ocupado': False}, -1: {'ocupado': False}, 0: {'ocupado': False},1: {'ocupado': False}, 2: {'ocupado': False}, 3: {'ocupado': False}}
deck = [{'name': "queen",  'mana': 7, 'atack': 4, 'life': 6},
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

# for dict in deck:
#     print(dict.get('name'))

jogo = classJogo()

for dict in jogo.deck:
    print(dict.get('name'))

#while inserirPosicao(0, 1):
#    print(tab)
#    chaves2 = [key for key, val in tab.items() if val['ocupado']]
#    print(chaves2)