import pygame

class classJogo(object):
	
	def __init__(self):
		self.canvas = pygame.display.set_mode([1280, 720])

	def fimTurno(self):
		pass
		
	def ataque(self):
		# atkUnico
		# atkDuplo
		# espCura
		# atkJogador
		pass

	def addMana(self):
		pass

	def addMao(self):
		pass

	def drawBoard(self):
		self.canvas.fill([173, 119, 12])
		m_top = pygame.draw.rect(self.canvas, [130, 89, 9], ([0,0],[1280,180]))
		line_top = pygame.draw.line(self.canvas, [153, 153, 153], [180,0], [180,180])
		linva_vida_top = pygame.draw.line(self.canvas, [153, 153, 153], [0, 90], [180,90])

		line_mid = pygame.draw.line(self.canvas, [153, 153, 153], [0,360], [1280,360])
		
		m_bot = pygame.draw.rect(self.canvas, [130, 89, 9], ([0,540],[1280,720]))
		line_bot = pygame.draw.line(self.canvas, [153, 153, 153], [180,540], [180,720])
		linva_vida_top = pygame.draw.line(self.canvas, [153, 153, 153], [0,630], [180,630])

