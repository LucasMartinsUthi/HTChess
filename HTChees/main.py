import pygame
import sys
from classe.classJogador import classJogador

pg = pygame
pg.init()

draw = pg.draw
image = pg.image
transform = pg.transform

jogador = classJogador()
print('teste print')
jogador.id = input("Qual Jogador vc é: ")

click = True
dragDrop = True
addCartaMesa = False
preview = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	jogador.initDraw()
	####################
	# EVENTOS DO MOUSE #
	####################
	# Click Button
	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click == True and jogador.button.collidepoint(pg.mouse.get_pos()):
		click = False
		jogador.addMao()
		jogador.drawMao()
		jogador.socket()
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

	#Preview
	h = -3
	chavesMesa = list(jogador.mesa.keys())
	chavesMesa.sort()
	for cartaMesa in chavesMesa:
		if dragDrop == False and addCartaMesa == True and jogador.mesa[cartaMesa]['colide'].collidepoint(pg.mouse.get_pos()):
			jogador.previewCartaMesa(h)
			preview = True	
		h += 1

	#Parado
	if (event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or dragDrop != False) and event.type != pygame.MOUSEMOTION:
		j = -3 
		chaves = list(jogador.mesa.keys())
		chaves.sort()	
		for casa in chaves:
			if jogador.mesa[casa]['colide'].collidepoint(pg.mouse.get_pos()):
				if addCartaMesa:
					jogador.addCartaMesa(j)	
					addCartaMesa = False
			j += 1
		jogador.cartaSelecionada = None
		dragDrop = True

	chaves = list(jogador.mesa.keys())
	for casa in chaves:
		if jogador.mesa[casa]['colide'].collidepoint(pg.mouse.get_pos()):
			colide = True
	if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and preview == True) or (dragDrop == False and not colide):
		preview = False
	colide = False

	#########
	# DRAWS #
	#########	
	jogador.drawMao()
	if not preview:
		jogador.drawMesa()
	jogador.drawDrag()
	jogador.drawInimigo()
	pg.display.update()
	pg.time.Clock().tick(60)


#(Socket)
#tornar multiplayer (testar com 2 comupatadores)
# desenhar as carta nos dois lados(Organizar funções do server e do client)

#(Terminar o resto do jogo)
# passsar turno / atacar / draw card
#remover cartas do tabuleiro
#Vida e Mana
#Fadiga
#Fim de Jogo

