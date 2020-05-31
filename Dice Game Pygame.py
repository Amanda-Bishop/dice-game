###########################################################
## File Name: Dice Game Pygame.py                        ##
## Description: Dice Game assignment in Pygame           ##
###########################################################
import pygame
pygame.init()
import inputbox
import random

#---------------------------------------#
# initialize global variables/constants #
#---------------------------------------#

BLUE = (196, 242, 255)
DARKYELLOW = (255, 251, 176)
YELLOW = (252, 250, 202)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
titleFont = pygame.font.SysFont("centurygothic", 55)
subTitleFont = pygame.font.SysFont("centurygothic", 25)
txtFont = pygame.font.SysFont("yugothicyugothicuilight", 20)

#------------------------------#
# function that rolls the dice #
#------------------------------#

def rollDice(numDice):
    rolledDice = []
    for d in range(numDice):
        rolledDice.append(random.randrange(1,7))
    return rolledDice

#----------------------------------------#
# function that determines the max score #
#----------------------------------------#

def maxScore(rolledDice):
    global run
    global stopCheck
    global score
    run = []
    noRepeats = list(set(rolledDice))
    for i in range(len(noRepeats)):
        num = noRepeats[i]
        if len(noRepeats) > 1:
            if (i > 0 and num - 1 == noRepeats[i-1]) or (i < len(noRepeats)-1 and num + 1 == noRepeats[i+1]):
                run.append(num)
                rolledDice.pop(rolledDice.index(num))
    if run == []:
        stopCheck = True
    newRun = []
    firstNum = 0
    for i in range(len(run)):   
        num = run[i]
        if i < len(run)-1 and num + 1 != run[i+1]:
            newRun = run[firstNum:i+1]
            firstNum = i + 1
            score += len(newRun) ** 2
    for num in newRun:
        if num in run:
            run.pop(run.index(num))
    score += len(run) ** 2
    print('the score is',score)
    return rolledDice

#----------------------------------#
# function that creates the inputs #
#----------------------------------#

def inputs():
    global players
    global dice
    global playTo
    global scores
    global isInputScreen
    global isGameScreen
    global roll
    global currentPlayer
    global isScoreScreen
    global guess
    if isGameScreen:
        guess = inputbox.ask(win, 'Input Guess: ')
        while guess.isdigit() != True:
            guess = inputbox.ask(win, 'Invalid input. Input Guess: ')
        isScoreScreen = True
        isGameScreen = False
    else:
        players = inputbox.ask(win, 'Number of players: ')
        while players.isdigit() == False:
            players = inputbox.ask(win, 'Invalid input. Input number of players: ')
        players = int(players)
        win.fill(BLUE)
        dice = inputbox.ask(win, 'Number of dice from 6-10: ')
        while dice.isdigit() == False or int(dice) < 6 or int(dice) > 10:
            dice = inputbox.ask(win, 'Invalid input. Input number of dice from 6-10: ')
        dice = int(dice)
        print('DICE', dice)
        win.fill(BLUE)
        roll =  rollDice(dice)
        print(roll)
        playTo = inputbox.ask(win, 'Score to play to: ')
        while playTo.isdigit() == False:
            playTo = inputbox.ask(win, 'Invalid input. Input score to play to: ')
        playTo = int(playTo)
        win.fill(BLUE)
        for p in range(players):
            scores.append(0)
        isInputScreen = False
        isGameScreen = True
    

#-------------------------------------#
# function that draws the game button #
#-------------------------------------#

def drawGameBtn(rect):
    yellow = DARKYELLOW
    x = rect[0]
    y = rect[1]
    width = rect[2]
    height = rect[3]
    if pygame.Rect((x, y, width, height)).collidepoint(pygame.mouse.get_pos()):
            yellow = YELLOW
    pygame.draw.rect(win, yellow, (x, y, width, height), 0)
    pygame.draw.rect(win, BLACK, (x, y, width, height), 2)
    txtSurface = subTitleFont.render('Play', True, BLACK)
    win.blit(txtSurface, (x + 5, y + 5))

#-------------------------------------------------------#
# function that returns if a button has been clicked on #
#-------------------------------------------------------#

def gameBtnClick(mp, button):
    if pygame.Rect(button).collidepoint(mp):
        return True
    return False

#-------------------------------------#
# function that draws the next button #
#-------------------------------------#

def drawNextBtn(rect):
    yellow = DARKYELLOW
    x = rect[0]
    y = rect[1]
    width = rect[2]
    height = rect[3]
    if pygame.Rect((x, y, width, height)).collidepoint(pygame.mouse.get_pos()):
            yellow = YELLOW
    pygame.draw.rect(win, yellow, (x, y, width, height), 0)
    pygame.draw.rect(win, BLACK, (x, y, width, height), 2)
    txtSurface = subTitleFont.render('Next Player', True, BLACK)
    win.blit(txtSurface, (x + 5, y + 5))

#-------------------------------------------------------#
# function that returns if a button has been clicked on #
#-------------------------------------------------------#

def nextBtnClick(mp, button):
    if pygame.Rect(button).collidepoint(mp):
        return True
    return False

#--------------------------------#
# function that loads the images #
#--------------------------------#

def loadDiceImages():
    dImages = []
    for imgNum in range(1,7):
        fileName = 'dice' + str(imgNum) + '.png'
        dImages.append(pygame.image.load(fileName))
    return dImages

#-----------------------------------#
# function that redraws all objects #
#-----------------------------------#
def drawWin():
    global dice
    global roll
    global score
    global guess
    win.fill(BLUE)
    x = 15
    y = 250
    if isMainScreen:
        txtSurface = titleFont.render('Dice Game', True, BLACK)
        win.blit(txtSurface, ((700 - txtSurface.get_width()) // 2, 200))
        drawGameBtn(playBtn)
    if isInputScreen:
        inputs()
    if isGameScreen:
        for d in roll:
            win.blit(dImages[d-1],(x,y))
            x+=110
            if len(roll)>6:
                if x >=590:
                    x=15
                    y+=110
        txtSurface = titleFont.render('Player '+str((currentPlayer + 1)), True, BLACK)
        win.blit(txtSurface, ((700 - txtSurface.get_width()) // 2, 50))
        inputs()
    if isScoreScreen:
        
        y = 50
        for i,score in enumerate(scores):
            txtSurface = txtFont.render('Player '+str(i + 1) + ' score: ' + str(score),True, BLACK)
            win.blit(txtSurface, ((700 - txtSurface.get_width()) // 2, y))
            y += 25
        drawNextBtn(nextBtn)
            
            
                    
    pygame.display.update()

#------------------------------#
# the main program begins here #
#------------------------------#

# Initializing the variables #
score = 0
stopCheck = False
run = []
roll = []
playBtn = (314,310,61,42)
nextBtn = (280,310,150,42)
players = 0
currentPlayer = 0
dice = 0
playTo = 0
scores = []
dImages = loadDiceImages()
guess = 0


# Game screens #
isMainScreen = True
isInputScreen = False
isGameScreen = False
isScoreScreen = False


win = pygame.display.set_mode((700,480))
inPlay = True
while inPlay:
    drawWin()
    pygame.time.delay(10)
    if isScoreScreen:
        while True:
            roll = maxScore(roll)
            if stopCheck == True:
                break
        print('score',score)
        if score == guess:
            scores[currentPlayer] += score
        score = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if isMainScreen:
                if gameBtnClick(mousePos, playBtn):
                    isMainScreen = False
                    isInputScreen = True
            if isScoreScreen:
                if nextBtnClick(mousePos, nextBtn):
                    currentPlayer += 1
                    if currentPlayer > players-1:
                        currentPlayer = 0
                    roll =  rollDice(dice)
                    print(roll)
                    isScoreScreen = False
                    isGameScreen = True
    

#---------------------------------------#                                        
pygame.quit()                           #
