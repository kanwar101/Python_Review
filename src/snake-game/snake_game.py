import pygame


pygame.init()
dis = pygame.display.set_mode((500,300))
pygame.display.update()


blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)

x1=200
y1 = 100

x1_change=0
y1_change=0

clock=pygame.time.Clock()

pygame.display.set_caption('Snake Game')
game_over = False
while not game_over:
	for event in pygame.event.get():
		#print (event)
		if event.type==pygame.QUIT:
			game_over=True
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				x1_change= -10
				y1_change= 0
			if event.key == pygame.K_RIGHT:
				x1_change = 10
				y1_change = 0
			if event.key == pygame.K_UP:
				x1_change= 0
				y1_change= -10
			if event.key == pygame.K_DOWN:
				x1_change = 0
				y1_change = 10

	x1 +=x1_change
	y1 +=y1_change
	dis.fill(white)

	pygame.draw.rect(dis, blue, [x1,y1,10,10])
	pygame.display.update()
	clock.tick (30)

pygame.quit()
quit()
