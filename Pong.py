import pygame
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (100, 124, 100)
font = pygame.font.SysFont('Microsoft YaHei', 48)
size = (1200, 600)
screen = pygame.display.set_mode(size)
titlename = pygame.image.load('PONGNAME.png')
startimage = pygame.transform.scale(pygame.image.load('start.png'),(200,100))
quitimage = pygame.transform.scale(pygame.image.load('quit.png'),(200, 100))
pauseimage = pygame.transform.scale(pygame.image.load('resume.png'),(200, 100))
restartimage = pygame.transform.scale(pygame.image.load('restart.png'),(200, 100))
intro = True
paused = False
done = False
moving = False
p1s = 0               #player1 score
p2s = 0               #player2 score
intro = True
paused = False
done = False
pygame.display.set_caption('PONG')

p1x = 250
p2x = 250
bx = 300
by = 600
p1y = 45
p2y = 1127
xchange1 = 0
xchange2 = 0

clock = pygame.time.Clock()


def p1(): 
    p1y = 45
    p1w = 25
    p1l = 120
    pygame.draw.rect(screen, white, [p1y, p1x, p1w, p1l])

def p2():
    p2y = 1127
    p2w = 25
    p2l = 120
    pygame.draw.rect(screen, white, [p2y, p2x, p2w, p2l])

def ball(by,bx):
    pygame.draw.ellipse(screen, white, [by, bx, 30, 30])



def ball(by, bx):
    pygame.draw.ellipse(screen, white, [by, bx, 40, 40])

def unpause():
    global paused
    paused = False

def pause():

    global  paused, moving
    while paused == True:
        for pausemenu in pygame.event.get():
            if pausemenu.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pausemenu.type == pygame.KEYDOWN:
                if pausemenu.key == pygame.K_SPACE:
                    unpause()


        button(pauseimage, (1200 - 200) / 2, 200, 200, 100, black, black, unpause)
        button(quitimage, (1200 - 200) / 2, 400, 200, 100, black, black, quit)
        button(restartimage, (1200-200)/2, 300, 200, 100, black, black, game_loop)
        pygame.display.update()
        clock.tick(60)

def scoreboard():
    score1 = font.render(p1s, False, green)
    score2 = font.render(p2s, False, green)
    screen.blit(score1, (200, 100))
    screen.blit(score2, (700, 100))


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
    global p1x, p2x, xchange2, xchange1, done, paused, moving, p1s, p2s

    check = random.randint(0, 1)
    if check == 0:
        by_change = 10
        bx_change = random.randint(-10, 10)
    if check == 1:
        by_change = -10
        bx_change = random.randint(-10, 10)

    if check == 0:
        by = p1y + 27
        bx = p1x + 45
    else:
        by = p2y - 32
        bx = p2x + 45
    while not done:
        for event in pygame.event.get():
            if moving == False:
                if event.type == pygame.KEYDOWN:
                    if check == 0:
                        if event.key == pygame.K_s or event.key == pygame.K_w:
                            moving = True
                    if check == 1:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            moving = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = True
                    pause()
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

        p1x = p1x + xchange1
        p2x = p2x + xchange2



        if moving == True:
            by += by_change
            bx += bx_change

        if bx >= 600 - 120 or bx <= 0:
            bx_change = - bx_change
        if by < 70:
            if p1x > bx and bx + 30 < p1x+120:
                by -= 10
                bx -= 10
                p2s += 1
                moving = False
            else:
                by_change = -by_change
                bx_change = random.randint(-10, 10)
        if by > 1127-30:
            if p2x > bx and bx+30 < p2x+120:
                by +=10
                bx += 10
                p1s += 1
                moving = False
            else:
                by_change = -by_change
                bx_change = random.randint(-10, 10)


        if p1x > 600 - 120:
            p1x = 600 - 120
        if p1x < 0:
            p1x = 0
        if p2x > 600 - 120:
            p2x = 600 -120
        if p2x < 0:
            p2x = 0

        screen.fill(black)
        scoreboard()
        p1()
        p2()
        ball(by,bx)

        pygame.display.update()
        clock.tick(60)

intro()
