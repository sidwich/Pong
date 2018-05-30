import pygame
import random
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (100, 124, 100)
size = (1200, 600)
screen = pygame.display.set_mode (size)
pygame.display.set_caption('PONG')

px = 250
def player():
    global px
    py = 45
    pw = 25
    pl = 120
    pygame.draw.rect(screen, white, [py, px, pw, pl])

def bot():
    by = 1127
    bx = 250
    bw = 25
    bl = 120
    pygame.draw.rect(screen, white, [by, bx, bw, bl])

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
        
        
        
        
        
