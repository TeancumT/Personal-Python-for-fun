'''

'''
import pygame
import random as ra

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Test")

win.fill((255, 255, 255))
x = 30
y = 30
width = 10
height = 10
velX = 0
velY = 0
run = True
a = True
b = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    # Y movement
    if (not keys[pygame.K_w]):
        if velY < 4:
            velY += 0.1
        y += velY
    elif keys[pygame.K_w]:
        if velY > -1:
            velY += -0.1
        y += velY
    if (y>(500-height)):
        y = 0
    if (y<0):
        y = 500-height
    # X movement
    if keys[pygame.K_d]:
        a = True
        b = False
    if keys[pygame.K_a]:
        a = False
        b = False
    if keys[pygame.K_s]:
        a = False
        b = True
    if b:
        velX = 0
    elif a:
        if velX < 6:
            velX += 0.1
        x += velX*(1+(ra.random()-1/2))
    else:
        if velX > -6:
            velX -= 0.1
        x += velX*(1+(ra.random()-1/2))
    if x<0:
        x=500-height
    if x>500-width:
        x = 0
    
    if ra.random() > 0.85:
        win.fill((255, 255, 255))
    pygame.draw.rect(win, (int(40*(ra.random())), int(100*(ra.random())), int(200*(ra.random()))), (x, y, width, height))
    pygame.display.update() 
