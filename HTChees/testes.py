import json

your_json = [{'name': "queen",  'mana': 7, 'atack': 4, 'life': 6, 'cor': [0, 0, 255]},
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

a = json.dumps(your_json, indent=4, sort_keys=True)
print(a)