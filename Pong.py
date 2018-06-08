import pygame
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (100, 124, 100)
orange = (255, 117, 58)
font = pygame.font.SysFont('Microsoft YaHei', 72)
font_win = pygame.font.SysFont('Microsoft YaHei', 256)
size = (1200, 600)
screen = pygame.display.set_mode(size)
titlename = pygame.image.load('PONGNAME.png')
startimage = pygame.transform.scale(pygame.image.load('start.png'), (200, 100))
quitimage = pygame.transform.scale(pygame.image.load('quit.png'), (200, 100))
pauseimage = pygame.transform.scale(pygame.image.load('resume.png'), (200, 100))
nextimage = pygame.transform.scale(pygame.image.load('next.png'), (200, 100))
restartimage = pygame.transform.scale(pygame.image.load('restart.png'), (200, 100))
intro = True
paused = False
done = False
moving = False
p1s = 0  # player1 score
p2s = 0  # player2 score
intro = True
paused = False
done = False
winner = False
pygame.display.set_caption('PONG')

p1x = 250
p2x = 250
bx = 300
by = 600
p1y = 45
p2y = 1127
xchange1 = 0
xchange2 = 0
p1r = 0
p2r = 0

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


def ball(by, bx):
    pygame.draw.ellipse(screen, white, [by, bx, 30, 30])


def unpause():
    global paused
    paused = False


def pause():
    global paused, moving
    while paused == True:
        for pausemenu in pygame.event.get():
            if pausemenu.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pausemenu.type == pygame.KEYDOWN:
                if pausemenu.key == pygame.K_SPACE:
                    paused = False

        button(pauseimage, (1200 - 200) / 2, 200, 200, 100, black, black, unpause)
        button(quitimage, (1200 - 200) / 2, 400, 200, 100, black, black, quit)
        button(restartimage, (1200 - 200) / 2, 300, 200, 100, black, black, game_loop)
        pygame.display.update()
        clock.tick(60)

def winround():
    global p1s, p2s, winner, p1r, p2r
    while winner == True:
        for pausemenu in pygame.event.get():
            if pausemenu.type == pygame.QUIT:
                pygame.quit()
                quit()
        w2r = font.render(str(p2r), True, orange)
        w1r = font.render(str(p2r), True, orange)
        screen.fill(black)

        if p1s >= 2:
            win1 = font_win.render("P1WIN!", True, orange)
            screen.blit(win1, (300, 50))
            p1r += 1
        if p2s >= 2:
            win2 = font_win.render("P2WIN!", True, orange)
            screen.blit(win2, (300, 50))
            p2r += 1

        screen.blit(w2r, (400, 500))
        screen.blit(w1r, (800, 500))
        p1()
        p2()
        scoreboard()
        button(quitimage, (1200 - 200) / 2, 400, 200, 100, black, black, quit)
        button(nextimage, (1200 - 200) / 2, 300, 200, 100, black, black, game_loop)
        pygame.display.update()
        clock.tick(60)

def winner_winner_chicken_dinner():
    global p1s, p2s, winner
    while winner == True:
        for pausemenu in pygame.event.get():
            if pausemenu.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)

        if p1r >= 2:
            win1 = font_win.render("P1WIN!", True, orange)
            screen.blit(win1, (300, 50))
        if p2r >= 2:
            win2 = font_win.render("P2WIN!", True, orange)
            screen.blit(win2, (300, 50))
        p1()
        p2()
        scoreboard()
        button(quitimage, (1200 - 200) / 2, 400, 200, 100, black, black, quit)
        button(restartimage, (1200 - 200) / 2, 300, 200, 100, black, black, game_loop)
        pygame.display.update()
        clock.tick(60)


def scoreboard():
    score1 = font.render(str(p1s), True, green)
    score2 = font.render(str(p2s), True, green)
    screen.blit(score1, (200, 50))
    screen.blit(score2, (1000, 50))


def button(img, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if mouse[0] >= x and mouse[0] <= x + w and mouse[1] >= y and mouse[1] <= y + h:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    screen.blit(img, (x, y))


def intro():
    global intro
    intro = True
    while intro:
        screen.fill(black)
        screen.blit(titlename, (300, 50))
        button(startimage, (1200 - 200) / 2, 300, 200, 100, black, black, game_loop)
        button(quitimage, (1200 - 200) / 2, 400, 200, 100, black, black, quit)
        for startmenu in pygame.event.get():
            if startmenu.type == pygame.QUIT:
                pygame.quit()
                quit()
        p1()
        p2()
        pygame.display.update()


def game_loop():
    global p1x, p2x, xchange2, xchange1, done, paused, moving, p1s, p2s, winner
    p1s = 0
    p2s = 0
    moving = False
    winner = False
    check = random.randint(0, 1)
    if check == 0:
        by_change = 10
        bx_change = random.randint(-10, 10)
    else:
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
                    xchange1 = 7
                if event.key == pygame.K_w:
                    xchange1 = -7
                if event.key == pygame.K_UP:
                    xchange2 = -7
                if event.key == pygame.K_DOWN:
                    xchange2 = 7
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

        if bx >= 600 - 30 or bx <= 0:
            bx_change = - bx_change

        if by <= 70 and by >= 70 - 10:
            if p1x <= bx and bx + 40 <= p1x + 140:
                by_change = -by_change
                bx_change = random.randint(-10, 10)

        if by >= 1127 - 30 and by <= 1127 - 30 + 10:
            if p2x <= bx and bx + 40 <= p2x + 140:
                by_change = -by_change
                bx_change = random.randint(-10, 10)

        if by <= 0:
            by = p2y - 32
            bx = p2x + 45
            p2s += 1
            moving = False
            check = 1
        if by >= 1200:
            by = p1y + 27
            bx = p1x + 45
            p1s += 1
            moving = False
            check = 0

        if p1x > 600 - 120:
            p1x = 600 - 120
        if p1x < 0:
            p1x = 0
        if p2x > 600 - 120:
            p2x = 600 - 120
        if p2x < 0:
            p2x = 0

        if p1s >= 2 or p2s >= 2:
            winner = True
            winround()

        screen.fill(black)
        scoreboard()
        p1()
        p2()
        ball(by, bx)

        pygame.display.update()
        clock.tick(60)


intro()

# 球的反弹问题， 有一部分物理模型无效
# p2发球问题， 出现glich
# 音效（静音？）
