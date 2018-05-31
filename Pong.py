
import pygame
import random
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (100, 124, 100)
size = (1200, 600)
screen = pygame.display.set_mode (size)
pygame.display.set_caption('PONG')

p1x = 250
p2x = 250
by = 600
bx = 300
xchange1 = 0
xchange2 = 0
def p1():
    global p1x
    p1y = 45
    p1w = 25
    p1l = 120
    pygame.draw.rect(screen, white, [p1y, p1x, p1w, p1l])

def p2():
    global p2x
    p2y = 1127
    p2w = 25
    p2l = 120
    pygame.draw.rect(screen, white, [p2y, p2x, p2w, p2l])

def ball():
    global bx, by
    pygame.draw.ellipse(screen, white, [by, bx, 30, 30])

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                pause = True
            if event.key == pygame.K_s:
                xchange1 = 5
            if event.key == pygame.K_w:
                xchange1 = -5
            if event.key == pygame.K_UP:
                xchange2 = -5
            if event.key == pygame.K_DOWN:
                xchange2 = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                xchange1 = 0
            if event.key == pygame.K_s:
                xchange1 = 0
            if event.key == pygame.K_UP:
                xchange2 = 0
            if event.key == pygame.K_DOWN:
                xchange2 = 0
    if p1x <= 600 or p1x >= 0:
        p1x = p1x + xchange1
    else:
        p1x = p1x
    if p2x <= 600 or p2x >= 0:
        p2x = p2x + xchange2
    else:
        p2x = p2x
    screen.fill(black)
    p1()
    p2()
    ball()
    pygame.display.update()
    clock.tick(60)



