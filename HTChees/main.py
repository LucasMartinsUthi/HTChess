import pygame
import sys
from classe.classJogador import classJogador
from classe.classJogo import classJogo

pg = pygame
pg.init()

draw = pg.draw
image = pg.image
transform = pg.transform

Jogo = classJogo()
Jogador = classJogador()


# Jogo.drawBoard()

# teste peao
# peao = image.load('img/b_peao.png')
# peao2 = transform.smoothscale(peao, (160,220))
# peao_r = peao2.get_rect()
click = True
for dict in Jogador.deck:
	print(dict['name'])

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# Jogo.canvas.blit(peao2, peao_r)
	carta = draw.rect(Jogo.canvas, [153, 153, 153], ([0,0],[200,200]))
	if carta.collidepoint(pg.mouse.get_pos()):
		carta = draw.rect(Jogo.canvas, [153, 0, 0], ([0,0],[200,200]))

	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click == True and carta.collidepoint(pg.mouse.get_pos()):
		click = False
		Jogador.addMao()
	elif event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or click != False:
		click = True

	pg.display.update()
	pg.time.Clock().tick(60)

# Loop com o draw do tabuleiro