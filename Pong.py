import pygame
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (100, 124, 100)
size = (1200, 600)
screen = pygame.display.set_mode(size)
titlename = pygame.image.load('PONGNAME.png')
startimage = pygame.transform.scale(pygame.image.load('start.png'),(200,100))
quitimage = pygame.transform.scale(pygame.image.load('quit.png'),(200, 100))
pauseimage = pygame.transform.scale(pygame.image.load('resume.png'),(200, 100))
intro = True
paused = False
pygame.display.set_caption('PONG')

p1x = 250
p2x = 250
bx = 300
by = 600
xchange1 = 0
xchange2 = 0

clock = pygame.time.Clock()
done = False

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
    pygame.draw.ellipse(screen, white, [by, bx, 40, 40])

def unpause():
    global paused
    paused = False

def pause():
    global  paused
    while paused == True:
        screen.fill(black)
        screen.blit(titlename, (300, 50))
        button(pauseimage, (1200 - 200) / 2, 300, 200, 100, black, black, unpause)
        button(quitimage, (1200 - 200) / 2, 400, 200, 100, black, black, quit)
        for startmenu in pygame.event.get():
            if startmenu.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(60)


def button(img,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if mouse[0] >= x and mouse[0] <= x + w and mouse[1] >= y and mouse[1] <= y + h:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    screen.blit(img,(x,y))


def intro():
    global intro
    intro = True
    while intro:
        screen.fill(black)
        screen.blit(titlename, (300, 50))
        button(startimage,(1200-200)/2,300,200,100,black,black,game_loop)
        button(quitimage, (1200-200)/2, 400, 200, 100, black,black,quit)
        for startmenu in pygame.event.get():
            if startmenu.type == pygame.QUIT:
                pygame.quit()
                quit()
        p1()
        p2()
        pygame.display.update()






def game_loop():
    global p1x, p2x, xchange2, xchange1, done, pause
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
        if p1x <= 600 - 120 or p1x >= 0:
            p1x = p1x + xchange1
        else:
            p1x = p1x
        if p2x <= 600 - 120 or p2x >= 0:
            p2x = p2x + xchange2
        else:
            p2x = p2x
        screen.fill(black)
        p1()
        p2()
        ball()
        pygame.display.update()
        clock.tick(60)

intro()
