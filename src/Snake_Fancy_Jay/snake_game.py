from pygame.locals import *
from random import randint
import time
import pygame


#main booleans
playing = True
moveUp = moveDown = moveRight = moveLeft = move_init = False

# other init libraries
step = 23
score = 0
length = 2
speed = 100

# list to store the co-ordinates of the snake
x_snake_position = [0]
y_snake_position = [0]

for i in range(0,1000):
	x_snake_position.append(-100)
	y_snake_position.append(-100)


def collision(x_coordinates_1,y_coordinates_1,x_coordinates_2,y_coordinates_2,snake_size,size_fruit):
	if ((x_coordinates_1 + snake_size >=x_coordinates_2) or (x_coordinates_1 >= x_coordinates_2)) and x_coordinates_1 <= x_coordinates_2 + size_fruit:
		if((y_coordinates_1 + snake_size >=y_coordinates_2) or (y_coordinates_1 >= y_coordinates_2)) and y_coordinates_1 <= y_coordinates_2 + size_fruit:
			return True
		return False

def disp_score(score):
	font = pygame.font.SysFont(None,25)
	text = font.render("Score:"+str(score),True,(0,0,0))
	window.blit(text,(400,0))


pygame.init()

#create the window
window = pygame.display.set_mode((800,500))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")

#Blit the image
cover = pygame.Surface(window.get_size())
cover = cover.convert()
cover.fill((250,250,250))
window.blit(cover,(0,0))

#Refresh everything
pygame.display.flip()

bruit_mouvement = pygame.mixer.Sound("move.wav")
bruit_collision = pygame.mixer.Sound("collision.wav")

head = pygame.image.load("head.png").convert_alpha()
head = pygame.transform.scale(head, (35,35))

body_part1 = pygame.image.load("corps.png").convert_alpha()
body_part1 = pygame.transform.scale(body_part1, (25,25))

fruit = pygame.image.load("fruit.png").convert_alpha()
fruit = pygame.transform.scale(fruit, (35,35))

# store the fruit and head cordniates
position_1 = head.get_rect()
position_fruit = fruit.get_rect()

# storing the variables in the list variables created before
x_snake_position[0] = position_1.x
y_snake_position[0] = position_1.y

position_fruit.x = randint(2,10)*step
position_fruit.y = randint(2,10)*step


while (playing == True):
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			playing = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if moveUp == False and move_init == True: 
					if moveDown == True:
						moveUp == False
					else:
						moveDown = moveRight = moveLeft = False 
						moveUp = move_init = True
						pygame.mixer.Sound.play(bruit_mouvement)

			if event.key == pygame.K_DOWN:
				if moveDown == False:
					if moveUp == True:
						moveDown == False
					else:
						moveRight = moveLeft = moveUp = False 
						moveDown = move_init = True
						pygame.mixer.Sound.play(bruit_mouvement)

			if event.key == pygame.K_RIGHT:
				if moveRight == False: 
					if moveLeft == True:
						moveRight == False
					else:
						moveLeft = moveUp = moveDown = False 
						moveRight = move_init = True
						pygame.mixer.Sound.play(bruit_mouvement)

			if event.key == pygame.K_LEFT:
				if moveLeft == False:
					if moveRight == True:
						moveLeft == False
					else:
						moveRight = moveDown = moveUp = False
						moveLeft = move_init = True
						pygame.mixer.Sound.play(bruit_mouvement)

	window.blit(body_part1, (-5,5))
	window.blit(head, (0,0))

	for i in range(length-1,0,-1):

		x_snake_position[i] = x_snake_position[(i-1)]
		y_snake_position[i] = y_snake_position[(i-1)]

	cover.fill((250, 250, 250)) 

	for i in range(1,length):
		cover.blit(body_part1, (x_snake_position[i], y_snake_position[i]))

	if moveUp:
		y_snake_position[0] = y_snake_position[0] - step 
		window.blit(cover, (0,0)) 
		window.blit(head, (x_snake_position[0], y_snake_position[0]))

	if moveDown:
		y_snake_position[0] = y_snake_position[0] + step
		window.blit(cover, (0,0))
		window.blit(head, (x_snake_position[0], y_snake_position[0]))

	if moveRight:
		x_snake_position[0] = x_snake_position[0] + step
		window.blit(cover, (0,0))
		window.blit(head, (x_snake_position[0], y_snake_position[0]))

	if moveLeft:
	 	x_snake_position[0] = x_snake_position[0] - step
	 	window.blit(cover, (0,0))
	 	window.blit(head, (x_snake_position[0], y_snake_position[0]))

	if x_snake_position[0] < window_rect.left:
		pygame.mixer.Sound.play(bruit_collision)
		playing = False

	if x_snake_position[0] + 35 > window_rect.right:
		pygame.mixer.Sound.play(bruit_collision)
		playing = False

	if y_snake_position[0] < window_rect.top:
		pygame.mixer.Sound.play(bruit_collision)
		playing = False
	if y_snake_position[0] + 35 > window_rect.bottom:
		pygame.mixer.Sound.play(bruit_collision)
		playing = False



	
	window.blit(fruit, position_fruit)

	if collision(x_snake_position[0], y_snake_position[0], position_fruit.x, position_fruit.y,35,25):
		position_fruit.x = randint(1,20)*step
		position_fruit.y = randint(1,20)*step

		for j in range(0,length):
			while collision(position_fruit.x, position_fruit.y, x_snake_position[j], y_snake_position[j],35,25):
				position_fruit.x = randint(1,20)*step   
				position_fruit.y = randint(1,20)*step
		length = length + 1
		score = score + 1

		

	disp_score(score)
	pygame.display.flip()
	time.sleep (speed / 1000)
pygame.quit()
exit()



	
		














						

						

						

			







