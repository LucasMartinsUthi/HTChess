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
addCartaMesa = False
preview = False
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	jogador.initDraw()

	# Click Button
	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click == True and jogador.button.collidepoint(pg.mouse.get_pos()):
		click = False
		jogador.addMao()
		preview = False;
	elif event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or click != False:
		click = True
		preview = False

	# Drag Drop carta
	i = 0
	for carta in jogador.mao:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and dragDrop == True and carta['rect'].collidepoint(pg.mouse.get_pos()):
			dragDrop = False
			jogador.cartaSelecionada = i
			addCartaMesa = True
		i += 1
		preview = True;

	#Preview
	h = -3
	chavesMesa = list(jogador.mesa.keys())
	chavesMesa.sort()
	for cartaMesa in chavesMesa:
		if dragDrop == False and addCartaMesa == True and jogador.mesa[cartaMesa]['rect'].collidepoint(pg.mouse.get_pos()):
			jogador.addCartaMesa(h, True)	
		h += 1

	#Parado
	if (event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or dragDrop != False) and event.type != pygame.MOUSEMOTION:
		j = -3 
		chaves = list(jogador.mesa.keys())
		chaves.sort()	
		for casa in chaves:
			if jogador.mesa[casa]['rect'].collidepoint(pg.mouse.get_pos()):
				if addCartaMesa:
					jogador.addCartaMesa(j)	
					addCartaMesa = False
			j += 1
		jogador.cartaSelecionada = None
		dragDrop = True
		preview = False

	jogador.drawMao()
	jogador.drawDrag()
	pg.display.update()
	print(preview)
	if not preview:
		jogador.drawMesa()
	pg.time.Clock().tick(60)

# Loop com o draw do tabuleiro
