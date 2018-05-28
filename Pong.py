import pygame
import random
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (100, 124, 100)
size = (1200, 600)
screen = pygame.display.set_mode (size)
pygame.display.set_caption('PONG')

px2 = 250
def player():
    global px2
    py1 = 45
    ph1 = 25
    ph2 = 120
    pygame.draw.rect(screen, white, [py1, px2, ph1, ph2])

def bot():
    by1 = 1127
    bx2 = 250
    bh1 = 25
    bh2 = 120
    pygame.draw.rect(screen, white, [by1, bx2, bh1, bh2])

player()
bot()
pygame.display.flip()

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame
