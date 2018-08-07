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


Jogo.drawBoard()

# teste peao
peao = image.load('img/b_peao.png')
peao2 = transform.smoothscale(peao, (160,220))
peao_r = peao2.get_rect()

print(peao,'\n', peao2,'\n', peao_r)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


	Jogo.canvas.blit(peao2, peao_r)
	pg.display.flip()


print(surface)




