
import time
import pygame
from random import randint

pygame.init()

#Declaring boolean variables
playing = True
moveUp = moveDown = moveRight = moveLeft = move_init = False


#int variables

step= 23 
score = 0 
length = 2
speed = 75

#lists to store the coordinates of snake

x_snake_position = [0]
y_snake_position = [0]


#Creating main window

windows = pygame.display.set_mode((500, 500))
windows_rect = windows.get_rect()
pygame.display.set_caption("Snake Charmer")

#Blitting on main windows

cover = pygame.Surface(windows.get_size())
cover = cover.convert()
cover.fill((250,250,250))
windows.blit(cover, (0,0))

#refresh screen to display
pygame.display.flip()

#loading the main images

head = pygame.image.load("Images/head.png").convert_alpha()
head = pygame.transform.scale(head, (35, 35))

body = pygame.image.load("Images/body.png").convert_alpha() 
body = pygame.transform.scale (body, (25,25))


fruit = pygame.image.load("Images/fruit.png").convert_alpha() 
fruit = pygame.transform.scale (fruit, (25,25))


position_1=head.get_rect()
position_fruit = fruit.get_rect()

x_snake_position[0] = position_1.x
y_snake_position[0] = position_1.y



#Giving random coordinates

position_fruit.x = randint (2,10)*step
position_fruit.y=  randint (2,10)*step




#increase the size of the list
for i in range (0,1000):
	x_snake_position.append (-100)
	y_snake_position.append(-100)


def collision (x_coordinates_1, y_coordinates_1, x_coordinates_2, y_coordinates_2, snake_size, fruit_size):
	if ((x_coordinates_1+snake_size >= x_coordinates_2) or (x_coordinates_1 >x_coordinates_2)) and x_coordinates_1 <= x_coordinates_2 + fruit_size:
		if ((y_coordinates_1 > y_coordinates_2) or (y_coordinates_1 + snake_size >= y_coordinates_2)) and y_coordinates_1 <= y_coordinates_2 + fruit_size:
			return True
		else:
			return False


# Display 
def disp_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render ("Score: " +str(score), True, (0,0,0))
    window.blit(text,(400,0))


#Main Loop

while (playing==True):
    # Collect all events

    for event in pygame.event.get():
        # check if user quits the game
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if moveUp == False and move_init == True:
                    if moveDown==True:
                        moveUp==False

                    else:
                        moveDown = moveRight = moveLeft = False

            if event.type == pygame.K_DOWN:
                if moveDown == False:
                    if moveUp == True:
                        moveDown == False
                    else:
                        moveRight=moveLeft=moveUp = False
                        moveDown = move_init=True

            if event.type == pygame.K_RIGHT:
                if moveRight == False:
                    if moveLeft == True:
                        moveRight == False
                    else:
                        moveLeft=moveUp=moveDown = False
                        moveRight = move_init=True

            if event.type == pygame.K_LEFT:
                if moveLeft == False:
                    if moveRight == True:
                        moveleft == False
                    else:
                        moveRight=moveDown=moveUp = False
                        moveLeft = move_init=True
    windows.blit(body, (-5,5))
    windows.blit(head,(0,0))

    for i in range (length-1,0,-1):
        x_snake_position[i] = x_snake_position[(i-1)]
        y_snake_position[i] = y_snake_position[(i-1)]
# Filling the window with white to erase the diff  parts of snake
        cover.fill((250,250,250))

    for i in range (1,length):
        print(length)
        cover.blit(body, (x_snake_position[i],y_snake_position[i]))

    if moveUp:

        y_snake_position[0] = y_snake_position[0] - step
        windows.blit(cover,(0,0))
        windows.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveDown:

        y_snake_position[0] = y_snake_position[0] + step
        windows.blit(cover,(0,0))
        windows.blit(head, (x_snake_position[0], y_snake_position[0]))


    if moveRight:

        x_snake_position[0] = x_snake_position[0] + step
        windows.blit(cover,(0,0))
        windows.blit(head, (x_snake_position[0], y_snake_position[0]))


    if moveLeft:

        x_snake_position[0] = x_snake_position[0] + step
        windows.blit(cover,(0,0))
        windows.blit(head, (x_snake_position[0], y_snake_position[0]))


    # Calling the collision function to check  if te snake hits the edge of window

    if x_snake_position[0] < windows_rect.left:
        playing = False

    if x_snake_position[0] +35 > windows_rect.right:
        playing=False

    if y_snake_position[0] +35 > windows_rect.bottom:
        playing=False

    if x_snake_position[0] < windows_rect.top:
        playing=False

    #Calling Collision Function

    if collision (x_snake_position[0],y_snake_position[0], x_snake_position[i], y_snake_position[i],0,0) and (move_init==True):
        playing=False

#Blitting the fruit

    windows.blit(fruit, position_fruit)

    # Calling the collision function to check if snake hits the fruit

    if collision (x_snake_position[0],y_snake_position[0],position_fruit.x, position_fruit.y,35,25):
        #Giving new coordinates to fruit when snake eats the fruit
        position_fruit.x = randint(1,20)*step
        position_fruit.y=randint(1,20)*step

        #giving new coordinates to fruit if ones given above are same as the snake's one
        for j in range(0,length):
            while collision(position_fruit.x, position_fruit.y, x_snake_position[j],35,25):
                position_fruit.x= randint(1,20)*step
                position_fruit.y = randint (1,20) *step

        # increasing length of the snake

        length=length+1
        score=score+1



    pygame.display.flip()    

