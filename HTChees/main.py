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
jogador = classJogador()

click = True
dragDrop = True

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# Click Button
	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click == True and jogador.button.collidepoint(pg.mouse.get_pos()):
		click = False
		jogador.addMao()
	elif event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or click != False:
		click = True

	# Drag Drop carta
	for carta in jogador.mao:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and dragDrop == True and carta['rect'].collidepoint(pg.mouse.get_pos()):
			dragDrop = False
			print('drag')

	pg.display.update()
	pg.time.Clock().tick(60)

# Loop com o draw do tabuleiro