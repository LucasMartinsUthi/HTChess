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
addCartaMesa = True

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
	i = 0
	for carta in jogador.mao:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and dragDrop == True and carta['rect'].collidepoint(pg.mouse.get_pos()):
			dragDrop = False
			jogador.cartaSelecionada = i
			addCartaMesa = True
		i += 1
	if (event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or dragDrop != False) and event.type != pygame.MOUSEMOTION:
		j = -3 		
		for casa in jogador.mesa:
			if jogador.mesa[casa]['rect'].collidepoint(pg.mouse.get_pos()):
				if addCartaMesa:
					jogador.addCartaMesa()	
					addCartaMesa = False
			j += 1
		jogador.cartaSelecionada = None
		dragDrop = True

	jogador.initDraw()
	jogador.drawMao()
	jogador.drawMesa()
	jogador.drawDrag()

	pg.display.update()
	pg.time.Clock().tick(60)

# Loop com o draw do tabuleiro
