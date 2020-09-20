#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Snake - v2.1
# Ce script est un programme du jeu snake
# License libre CC BY 4.0
# Colin Laganier - Thomas Le Menestrel - 2018.05.13

#Importing the necessary libraries
from pygame.locals import *
from random import randint
import pygame
import time

#Definition of the variables involved in the game
x = [0]
y = [0]
step = 23
score = 0
highscore = 0
length = 3
etat = 1
menu = 1
size_barre = 70
vitesse = 75.0

#Creation of a large number of ranks within the list to possibly enlarge the body of the snake up to 1000 sections
for i in range(0,1000):
    x.append(-100)
    y.append(-100)

#Function defining if there is a collision between the coordinates of the snake and other coordinates, such as those of fruits or different parts of the snake
def collision(x1,y1,x2,y2, size_snake, size_fruit):
    if ((x1 + size_snake >= x2) or (x1 >= x2)) and x1 <= x2 + size_fruit:
        if ((y1 >= y2) or (y1 + size_snake >=y2)) and y1 <= y2 + size_fruit:
            return True
        return False

#Function that displays the player's score on the game page
def disp_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, (0, 0, 0))
    window.blit(text,(400,0))

#Function that centers the given text between two coordinates
def disp_text(info,x,y):
    font18 = pygame.font.SysFont(None, 18)
    text = font18.render((info),True,(0,0,0))
    textX = text.get_rect().width
    textY = text.get_rect().height
    window.blit(text,((x - (textX / 2)),(y - (textY / 2))))

#Initializing the Pygame Libraries
pygame.init()

#Loading game sounds
bruit_mouvement = pygame.mixer.Sound("move.wav")
bruit_collision = pygame.mixer.Sound("collision.wav")

#Window creation
window = pygame.display.set_mode((500, 500))
window_rect = window.get_rect()

#The game window is named
pygame.display.set_caption("Snake")

#Loading a white background with which the window is filled
blanket = pygame.Surface(window.get_size())
blanket = blanket.convert()
blanket.fill((250, 250, 250))
window.blit(blanket, (0,0))

#Loading images of different game objects
head = pygame.image.load("head.png").convert_alpha() # The head
head = pygame.transform.scale(head, (35,35))
corps1 = pygame.image.load("corps.png").convert_alpha() #The body
corps1 = pygame.transform.scale(corps1, (25,25))
fruit = pygame.image.load("fruit.png").convert_alpha() #The fruit
fruit = pygame.transform.scale(fruit, (35,35))

#Recovery of their position
position_1 = head.get_rect()
position_fruit = fruit.get_rect()

#Insertion of the coordinates of the head in their respective list
x[0] = position_1.x
y[0] = position_1.y

#Random position is given to the first fruit, close to the player
position_fruit.x = randint(2,10)*step
position_fruit.y = randint(2,10)*step

#Screen refresh
pygame.display.flip()

#Variable that continues the main game loop
continuer = True
depUp = depDown = depRight = depLeft = move_init = False
#Changing the displacement variable
while(continuer):
    for event in pygame.event.get(): #Retrieving the various player events
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):#Checking if the player does not quit the game
            continuer = False
        if event.type == pygame.KEYDOWN:#Checking if the player is pressing one of the keys on the keyboard

            if event.key == pygame.K_UP:
                if etat == 2: #Checking if the program is in the playing state
                    if depUp == False and move_init == True:#Checking that the direction is different and announcing that the movements have started
                        if depDown == True:# Prevention of going in the opposite direction
                            depUp == False
                        else:
                            depDown = depRight = depLeft = False #Changing the displacement variable
                            depUp = move_init = True
                            pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_DOWN:
                if etat == 2:
                    if depDown == False:# Prevention of going in the opposite direction
                        if depUp == True:
                            depDown == False
                        else:
                            depRight = depLeft = depUp = False #Changing the displacement variable
                            depDown = move_init = True
                            pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_RIGHT:
                if etat == 1 and menu == 3:
                    if size_barre >=0 and size_barre <=130:
                        size_barre = size_barre + 10
                        vitesse = vitesse - 7.5
                if etat == 2:
                    if depRight == False: # Prevention of going in the opposite direction
                        if depLeft == True:
                            depRight == False
                        else:
                            depLeft = depUp = depDown = False #Changing the displacement variable
                            depRight = move_init = True
                            pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_LEFT:
                if etat == 1 and menu == 3:
                    if size_barre >=10 and size_barre <=140:
                        size_barre = size_barre - 10
                        vitesse = vitesse + 7.5
                if etat == 2:
                    if depLeft == False:
                        if depRight == True:# Prevention of going in the opposite direction
                            depLeft == False
                        else:
                            depRight = depDown = depUp = False #Changing the displacement variable
                            depLeft = move_init = True
                            pygame.mixer.Sound.play(bruit_mouvement)

            if event.key == pygame.K_RETURN:
                #Fill the screen blank to erase previous body parts
                blanket.fill((250,250,250))
                window.blit(blanket, (0,0))
                pygame.display.flip()

                if etat == 1:
                    etat = 2

                #Reset all game settings to the initial ones for the new game
                if etat == 3:
                    depUp = depDown = depRight = depLeft = move_init = False
                    length = 3
                    for i in range (2, 1000):
                        x[i] = y[i] = -100
                    x[0] = y[0] = 0
                    x[1] = -5
                    y[1] = 5
                    position_fruit.x = randint(2,10)*step
                    position_fruit.y = randint(2,10)*step
                    score = 0
                    etat = 2

            #Definition of a command to return to the start menu after playing
            if event.key == pygame.K_SPACE:
                if etat == 1:
                    if menu == 2 or menu == 3 or menu == 4:
                        menu = 1
                if etat == 3: #If the player loses
                    depUp = depDown = depRight = depLeft = move_init = False #Displacement variables become false
                    length = 3 #Reset all game settings to the initial ones for the new game
                    for i in range (2, 1000):
                        x[i] = y[i] = -100
                    x[0] = y[0] = 0
                    x[1] = -5
                    y[1] = 5
                    position_fruit.x = randint(2,10)*step
                    position_fruit.y = randint(2,10)*step
                    score = 0
                    etat = menu = 1

            if event.key == pygame.K_c: #Access to the controls page
                if etat == 1 and menu == 1:
                    menu = 2

            if event.key == pygame.K_p:#Access to the settings page
                if etat == 1 and menu == 1:
                    menu = 3

            if event.key == pygame.K_r:#Possibility to reset the speed to its initial value
                if etat == 1 and menu == 3:
                    size_barre = 70
                    vitesse = 75.0
            if event.key == pygame.K_w:#Access to the credits page
                if etat == 1 and menu == 1:
                    menu = 4

    #Main Menu Status
    if etat == 1:

        #Loading the menu wallpaper
        blanket_menu = pygame.image.load("fond2.png").convert()
        window.blit(blanket_menu, (0,0))

        if menu == 1:
            #Square is designed to give information to the player
            pygame.draw.rect(window,(0,255,0),(290,290,200,200))
            pygame.draw.rect(window,(0,200,0),(290,290,200,200),5)

            #Explanation to the player of how to enter the game
            disp_text("Press Enter to play",390,320)

            #Explain to the player which keys to use to play
            disp_text("Press C to see the",390,360)
            disp_text("orders",390,380)
            disp_text("Press P for",390,420)
            disp_text("settings",390,440)
            font14 = pygame.font.SysFont(None, 14)
            text = font14.render("Press W for credits",True,(0,0,0))
            window. blit(text, (320,470))
            pygame.display.flip()

        if menu == 2:
            #Square is designed to give information to the player
            pygame.draw.rect(window,(0,255,0),(290,290,200,200))
            pygame.draw.rect(window,(0,200,0),(290,290,200,200),5)

            #Explanation to the player how to play
            disp_text("Game controls :",390,310)
            font18 = pygame.font.SysFont(None, 18)
            text = font18.render("Travel :",True,(0,0,0))
            window. blit(text, (300,330))
            controls = pygame.image.load("keypad.png").convert_alpha()
            controls = pygame.transform.scale(controls, (90,80))
            window.blit(controls, (340,350))
            disp_text("Press esc to exit the",390,445)
            disp_text("Game",390,460)

            #Explanation to the player how to exit the menus
            font15 = pygame.font.SysFont(None, 15)
            text = font15.render(("Press space to return"),True,(0,0,0))
            window.blit(text,(305,475))
            pygame.display.flip()

        if menu == 3:
            #Square is designed to give information to the player
            pygame.draw.rect(window,(0,255,0),(290,290,200,200))
            pygame.draw.rect(window,(0,200,0),(290,290,200,200),5)

            #Setting up the slider to change the speed of the snake
            disp_text("Movement speed :",390,320)
            pygame.draw.rect(window,(235,51,36),(320,350,size_barre,15))
            pygame.draw.rect(window,(0,200,0),(320,350,140,15),3)
            disp_text("Press <- and -> to modify",390,380)
            disp_text("Press R for",390,430)
            disp_text("initial settings",390,450)
            font15 = pygame.font.SysFont(None, 15)

            #Explanation to the player how to exit the menus
            text = font15.render(("Press space to return"),True,(0,0,0))
            window.blit(text,(305,475))
            pygame.display.flip()

        if menu == 4:
            #Square is designed to give information to the player
            pygame.draw.rect(window,(0,255,0),(290,290,200,200))
            pygame.draw.rect(window,(0,200,0),(290,290,200,200),5)

            #Representation of information
            disp_text("Credits:",390,310)
            disp_text("Snake head image: MegaPixel",390,350)
            disp_text("Movement noise: Jeckkech",390,380)
            disp_text("Collision noise: ProjectsU012",390,410)
            disp_text("See README.md for links",390,440)

            #Explanation to the player how to exit the menus
            font15 = pygame.font.SysFont(None, 15)
            text = font15.render(("Press space to return"),True,(0,0,0))
            window.blit(text,(305,475))
            pygame.display.flip()

    #Current game state
    if etat == 2:

        #Loading items into the game
        window.blit(corps1, (-5,5))
        window.blit(head, (0,0))

        #Coordinates of the previous song given to each song
        for i in range(length-1,0,-1):
            x[i] = x[i-1]
            y[i] = y[i-1]

        blanket.fill((250, 250, 250)) #Fill the screen blank to erase previous body parts
        for i in range(1,length): #Loading the body of the snake
            blanket.blit(corps1, (x[i], y[i]))

        # Changing the position of the snake's head
        if depUp:
            y[0] = y[0] - step #Moving the head position
            window.blit(blanket, (0,0)) #Loading the wallpaper, the head
            window.blit(head, (x[0], y[0]))

        if depDown:
            y[0] = y[0] + step
            window.blit(blanket, (0,0))
            window.blit(head, (x[0], y[0]))

        if depRight:
            x[0] = x[0] + step
            window.blit(blanket, (0,0))
            window.blit(head, (x[0], y[0]))

        if depLeft:
            x[0] = x[0] - step
            window.blit(blanket, (0,0))
            window.blit(head, (x[0], y[0]))

        #Check that the snake does not touch the edges
        if x[0] < window_rect.left:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3
        if x[0] + 35 > window_rect.right:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3
        if y[0] < window_rect.top:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3
        if y[0] + 35 > window_rect.bottom:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3

        #Loading the fruit
        window.blit(fruit, position_fruit)

        #Checking if the snake touches a fruit
        if collision(x[0], y[0], position_fruit.x, position_fruit.y,35,25):
            position_fruit.x = randint(1,20)*step   #Nouvelles coordonnées du fruit lorsqu'il est "mangé"
            position_fruit.y = randint(1,20)*step
            for j in range(0,length):
            	while collision(position_fruit.x, position_fruit.y, x[j], y[j],35,25):
            		position_fruit.x = randint(1,20)*step   #Nouvelles coordonnées du fruit si les premieres insérés ont les même coordonnées que le corps du serpent
            		position_fruit.y = randint(1,20)*step
            length = length + 2
            score = score + 1

        #Checking if the snake's head touches a piece of the body
        
        if collision(x[0], y[0], x[i], y[i],0,0) and move_init:
            pygame.mixer.Sound.play(bruit_collision)
            etat = 3

        #Add score to screen
        disp_score(score)
        #Definition of the best score among the games played
        if score > highscore:
            highscore = score

        pygame.display.flip()

        #Adding a delay to the loop to achieve the desired travel speed
        time.sleep (vitesse / 1000.0)

    #State of the game completed
    if etat == 3:

        #Loading a frame to give information to the player
        pygame.draw.rect(window,(0,255,0),(150,150,200,200))
        pygame.draw.rect(window,(0,200,0),(150,150,200,200),5)

        #Loading the score of the game completed in the frame
        disp_text("Score: " + str(score),250,180)

        #Loading the best score among the games achieved in the frame
        disp_text("Best score : " + str(highscore),250,230)

        #Explanation to the player for how to replay
        disp_text("To replay press Enter !",250, 280)

        #Explanation to the player on how to return to the menu
        disp_text("To return to the menu press", 250,305)
        disp_text("on the space bar !",250,320)

        pygame.display.flip()

#Sortie du jeu
pygame.quit()
