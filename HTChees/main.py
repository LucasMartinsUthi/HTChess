import pygame
import sys
from classe.classJogador import classJogador

pg = pygame
pg.init()

draw = pg.draw
image = pg.image
transform = pg.transform

jogador = classJogador()
jogador.id = input("Qual Jogador vc é: ")

click = False
dragDrop = True
dragCavalo = True
addCartaMesa = False
preview = False
inicioTurno = True
primeiroTurno = True

jogador.socket()
jogador.addMao()
jogador.addMao()
jogador.addMao()

if int(jogador.inimigo['turno']) == int(jogador.id):
	jogador.addMao()

jogador.drawMao()

#Tela de Escolha de carta
escolhendoCarta = True
escolha = True
while escolhendoCarta:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	i = 0
	for carta in jogador.mao:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and escolha == True and carta['rect'].collidepoint(pg.mouse.get_pos()):
			if i in jogador.escolha:
				jogador.escolha.remove(i)
			else:
				jogador.escolha.append(i)
			escolha = False
		i += 1

	if (event.type != pygame.MOUSEBUTTONDOWN or event.button != 1) and event.type != pygame.MOUSEMOTION:
		escolha = True

	jogador.initDraw("Trocar")
	jogador.drawEscolha()
	pg.display.update()
	pg.time.Clock().tick(60)

	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and jogador.button.collidepoint(pg.mouse.get_pos()):
		jogador.trocaEscolha()
		escolhendoCarta = False

# Add Carta de Mana para jogador número 2
if int(jogador.inimigo['turno']) != int(jogador.id):
	jogador.addMaoMana()
	jogador.drawMao()
	primeiroTurno = False

# Tela jogo
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	if int(jogador.inimigo['turno']) != int(jogador.id):
		jogador.initDraw("T Inimigo")
	elif jogador.inimigo == None:
		jogador.initDraw("...")
	else:
		jogador.initDraw("Turno")

		# Click Button
		if inicioTurno:
			if not primeiroTurno:
				jogador.addMao()
				jogador.defesaInimigo()
			jogador.addMana()
			primeiroTurno = False
			inicioTurno = False

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click and escolhendoCarta != False and jogador.button.collidepoint(pg.mouse.get_pos()):
			print('passou Turno')
			click = False
			jogador.atackBispo()
			jogador.socket(True)
			inicioTurno = True

		elif event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or click != False:
			click = True
			escolhendoCarta = True

		# Drag Drop carta
		i = 0
		for carta in jogador.mao:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and dragDrop and carta['rect'].collidepoint(pg.mouse.get_pos()):
				dragDrop = False
				jogador.cartaSelecionada = i
				jogador.drag = [pygame.mouse.get_pos()[0] - 50, 720 - pygame.mouse.get_pos()[1] - 90]
				addCartaMesa = True
			i += 1

		# Drag Cavalo
		chavesMesa = [key for key, val in jogador.mesa.items() if val['ocupado']]
		for carta in chavesMesa:
			print("Carta:", carta, (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and dragCavalo and jogador.mesa[carta]['ocupado']['name'] == 'knight' and jogador.mesa[carta]['rect'].collidepoint(pg.mouse.get_pos()) and jogador.mesa[carta]['ocupado'] != False))
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and dragCavalo and jogador.mesa[carta]['ocupado']['name'] == 'knight' and jogador.mesa[carta]['rect'].collidepoint(pg.mouse.get_pos()) and jogador.mesa[carta]['ocupado'] != False:
				dragCavalo = False
				jogador.dragCavalo = [pygame.mouse.get_pos()[0] - 50, 720 - pygame.mouse.get_pos()[1] - 90]
				jogador.cavaloSelecionado = carta

		print("Ao final do loop - Selecionado", jogador.cavaloSelecionado, "Drag:", dragCavalo)

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
			chaves = list(jogador.mesa.keys())
			chaves.sort()	
			for casa in chaves:
				if jogador.mesa[casa]['colide'].collidepoint(pg.mouse.get_pos()):
					if addCartaMesa:
						jogador.addCartaMesa(casa)	
						addCartaMesa = False

			jogador.cartaSelecionada = None
			jogador.drag = False
			dragDrop = True

		#Cavalo
		if (event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or dragCavalo != False) and event.type != pygame.MOUSEMOTION:
			# chaves = list(jogador.mesa.keys())
			# chaves.sort()	
			# for casa in chaves:
			# 	if jogador.mesa[casa]['colide'].collidepoint(pg.mouse.get_pos()):
			# 		if addCartaMesa:
			# 			jogador.addCartaMesa(casa)	
			# 			addCartaMesa = False
						
			jogador.cavaloSelecionado = None
			jogador.dragCavalo = False
			dragCavalo = True

		chaves = list(jogador.mesa.keys())
		for casa in chaves:
			if jogador.mesa[casa]['colide'].collidepoint(pg.mouse.get_pos()):
				colide = True
		if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and preview == True) or (dragDrop == False and not colide):
			preview = False
		colide = False

		if jogador.drag != False:
			jogador.drag = [pygame.mouse.get_pos()[0] - 50, 720 - pygame.mouse.get_pos()[1] - 90]

		if jogador.dragCavalo != False:
			jogador.dragCavalo = [pygame.mouse.get_pos()[0], 720 - pygame.mouse.get_pos()[1]]
	#Draws 
	jogador.drawMao()
	if not preview:
		jogador.drawMesa()
	jogador.drawInimigo()
	jogador.drawDrag()
	if not dragCavalo:
		jogador.previewCavalo()
	pg.display.update()
	pg.time.Clock().tick(60)


#(Terminar o resto do jogo)
	#Fim de Jogo
	#Cavalo

# Animacao classe com os loop
