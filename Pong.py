import pygame                                                    #import moudle pygame
import random                                                    #import moudle random

pygame.init()
white = (255, 255, 255)                                          #define a color with red, green and blue
black = (0, 0, 0)
green = (100, 124, 100)
orange = (255, 117, 58)
font = pygame.font.SysFont('Microsoft YaHei', 72)             # define a font, use a font and size
font_win = pygame.font.SysFont('Microsoft YaHei', 256)
font_ins = pygame.font.SysFont('Microsoft Yahei', 48)
size = (1200, 600)                                              #define the size of screen
screen = pygame.display.set_mode(size)                          #show the screen
titlename = pygame.image.load('PONGNAME.png')                  #load image
startimage = pygame.transform.scale(pygame.image.load('start.png'), (200, 100))
quitimage = pygame.transform.scale(pygame.image.load('quit.png'), (200, 100))
pauseimage = pygame.transform.scale(pygame.image.load('resume.png'), (200, 100))
nextimage = pygame.transform.scale(pygame.image.load('next.png'), (200, 100))
restartimage = pygame.transform.scale(pygame.image.load('restart.png'), (200, 100))

pygame.mixer.music.load('startmenu.mp3')
intro = True                                                    #define variables
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

p1x = 250                                                           #the distance of pad player1 (left one) to the axis-x
p2x = 250                                                           #the distance of player2 to the axis-x
bx = 300                                                            #the distance of ball to axis-x
by = 600                                                            #the distance of ball to axis-y
p1y = 45                                                            #the distance of player1 to axis-y
p2y = 1127                                                          #the distance of  player2 to axis-y
xchange1 = 0                                                        #the change to player 1 in axis-x
xchange2 = 0                                                        #the change of player2 in axis-y
p1r = 0                                                             #player 1 win rounds
p2r = 0                                                             #player 2 win rounds\
high_score1 = 0
high_score2 = 0
v_high_score1 = 0
v_high_score2 = 0

clock = pygame.time.Clock()                                         #define clock

def highScore(p1s,p2s):
    global high_score1, high_score2
    config = open ("highScore.txt", "r")
    configDataStr = config.readlines()
    high_score1 = int(configDataStr[0])
    high_score2 = int(configDataStr[1])

#set funtion: rewrite high score
def rewrite_highScore(p1s,p2s):
    global v_high_score1,v_high_score2
    config = open("highScore.txt", "r+")
    if p1s > high_score1:
        config.write(str(p1s))
        v_high_score1 = p1s
    else:
        v_high_score1 = high_score1

    if p1s > high_score2:
        config.write(str(p2s))
        v_high_score2 = p2s
    else:
        v_high_score2 = high_score2

def p1():                                                           #define player1 the pad
    p1y = 45
    p1w = 25
    p1l = 120
    pygame.draw.rect(screen, white, [p1y, p1x, p1w, p1l])           #draw the rect


def p2():                                                           #defie the function of player2
    p2y = 1127
    p2w = 25
    p2l = 120
    pygame.draw.rect(screen, white, [p2y, p2x, p2w, p2l])           #draw player2


def ball(by, bx):
    pygame.draw.ellipse(screen, white, [by, bx, 30, 30])            #draw the ball


def unpause():                                                      #define unpause,
    global paused
    paused = False


def pause():                                                        #the function that control to pause
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

def winround():                                                        #set to get into next level
    global p1s, p2s, winner, p1r, p2r, p1l, p2l
    while winner == True:
        for pausemenu in pygame.event.get():
            if pausemenu.type == pygame.QUIT:
                pygame.quit()
                quit()
        w2r = font.render(str(p2r), True, orange)
        w1r = font.render(str(p1r), True, orange)
        screen.fill(black)

        if p1s >= 11:
            win1 = font_win.render("P1WIN!", True, orange)
            screen.blit(win1, (300, 50))
        if p2s >= 11:
            win2 = font_win.render("P2WIN!", True, orange)
            screen.blit(win2, (300, 50))
        screen.blit(w1r, (400, 500))
        screen.blit(w2r, (800, 500))
        highScoreword = font_ins.render("highscore:" + str(high_score1) + "-" + str(high_score2), True, white)
        screen.blit(highScoreword,(200, 200))
        p1()
        p2()
        scoreboard()
        rewrite_highScore(p1s, p2s)
        button(quitimage, (1200 - 200) / 2, 400, 200, 100, black, black, quit)
        button(nextimage, (1200 - 200) / 2, 300, 200, 100, black, black, nextlevel)
        pygame.display.update()
        clock.tick(60)


def scoreboard():                                                   #set to show and record the score
    score1 = font.render(str(p1s), True, green)
    score2 = font.render(str(p2s), True, green)
    screen.blit(score1, (200, 50))
    screen.blit(score2, (1000, 50))


def button(img, x, y, w, h, ic, ac, action=None):                    #set a function  for button
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if mouse[0] >= x and mouse[0] <= x + w and mouse[1] >= y and mouse[1] <= y + h:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    screen.blit(img, (x, y))


def intro():                                                         #set to the start menu
    global intro
    intro = True
    while intro:
        pygame.mixer.music.play(-1)
        screen.fill(black)
        screen.blit(titlename, (300, 50))
        button(startimage, (1200 - 200) / 2, 300, 200, 100, black, black, game_loop)
        button(quitimage, (1200 - 200) / 2, 400, 200, 100, black, black, quit)
        for startmenu in pygame.event.get():
            if startmenu.type == pygame.QUIT:
                pygame.quit()
                quit()
        instruction = font_ins.render('p1: w = up s = down         p2: uparrow = up  downarrow = down', True, green)
        screen.blit(instruction,(100, 0))

        p1()
        p2()
        pygame.display.update()


def game_loop():                                                #set into game
    global p1x, p2x, xchange2, xchange1, done, paused, moving, p1s, p2s, winner, p1r, p2r, p1l, p2l
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

        if p1s >= 11 or p2s >= 11:
            if p1s >= 2:
                p1r += 1
                winner = True
                winround()
                p2l = 80
            if p2s >= 2:
                p2r += 1
                winner = True
                winround()
                p1l = 80

        screen.fill(black)
        scoreboard()
        p1()
        p2()
        ball(by, bx)

        pygame.display.update()
        clock.tick(60)

def nextlevel():                #the second level of the game
    global p1x, p2x, xchange2, xchange1, done, paused, moving, p1s, p2s, winner, p1r, p2r, p1l, p2l
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
                    xchange1 = 10
                if event.key == pygame.K_w:
                    xchange1 = -10
                if event.key == pygame.K_UP:
                    xchange2 = -10
                if event.key == pygame.K_DOWN:
                    xchange2 = 10
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

        if p1s >= 11 or p2s >= 11:
            if p1s >= 2:
                p1r += 1
                winner = True
                winround()
                p2l = 80
            if p2s >= 2:
                p2r += 1
                winner = True
                winround()
                p1l = 80

        screen.fill(black)
        scoreboard()
        p1()
        p2()
        ball(by, bx)

        pygame.display.update()
        clock.tick(90)

intro()                       #run start menu
highScore()
print(high_score1, high_score2)
