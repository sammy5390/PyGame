import pygame

FPS=60

WIDTH=500
HEIGHT=600

WHITE=(255,255,255)
GREEN=(0,255,0)

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Galaxy")
clock=pygame.time.Clock()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((50,40))
		self.image.fill(GREEN)
		self.rect=self.image.get_rect()
		self.rect.x=200
		self.rect.y=200

running=True

while running:
	clock.tick(FPS)
	
	# input
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
			
	# update
	
	
	# display
	screen.fill(WHITE)
	pygame.display.update()
			
			
pygame.quit()
