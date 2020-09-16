import pygame

pygame.init()
dis = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Helicopter")

done = False

clock = pygame.time.Clock()

# Load Image Here
heli_left = pygame.image.load("heli_left.png")
heli_left = pygame.transform.scale(heli_left, (64, 64))
heli_right = pygame.image.load("heli_right.png")
heli_right = pygame.transform.scale(heli_right, (64, 64))

# initialize some variables
x = 25
y = 25
dx = 0
dy = 0
up_key = False
looking = 'right'
while not done:

    # Game Update placeholder

    if up_key:
        dy = dy - 0.5
    else:
        dy = dy + 0.5

    if dy > 7:
        dy = 7
    last_x = x
    last_y = y
    x += dx
    heli_rect=pygame.Rect(x,y,64,64)
    platform_rect=pygame.Rect(100,300,200,30)
    if heli_rect.colliderect(platform_rect):
        x=last_x
        dx=0

    y += dy
    heli_rect=pygame.Rect(x,y,64,64)
    platform_rect=pygame.Rect(100,300,200,30)
    if heli_rect.colliderect(platform_rect):
        y=last_y
        dy=0


    if x > 640:
        x = -64
    if y > 480-64:
        y=480-64
        dy=0

    # Keyboar and Mouse here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                looking='right'
                dx = 5
            if event.key == pygame.K_LEFT:
                looking='left'
                dx = -5
            if event.key == pygame.K_UP:
                up_key = True
                dy = -2
            if event.key == pygame.K_DOWN:
                dy = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                dx = 0
            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_UP:
                up_key = False
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = 0

    dis.fill((255, 255, 255))

    # Draw Here
    pygame.draw.rect(dis,(0,0,0),(0,0,639,479),2)
    pygame.draw.rect(dis,(0,150,0),(100,300,200,30))
    if looking == 'right':
        dis.blit(heli_right, (x, y))
    else:
        dis.blit(heli_left, (x,y))

    # Display what we draw here

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
