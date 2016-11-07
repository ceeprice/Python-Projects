from graphics import *
from random import random
from random import randint
import time
import _tkinter

try:  # import as appropriate for 2.x vs. 3.x
   import tkinter as tk
except:
   import Tkinter as tk

data = open("data.txt", "r")
numbers = data.readlines()
currentEntry = 0
gameScore = 0
currentLives = 3
play = True
result = "win"

size = 800

window = GraphWin("Dodge the Pumpkin", size, size)
width = window.getWidth()
height = window.getHeight()

window.setBackground(color_rgb(94, 144, 145))
moon = Circle(Point(width-160, 160), 150)
moon.setFill(color_rgb(175, 199, 199))
moon.setOutline(color_rgb(175, 199, 199))
ghost = Image(Point(width/2, height-50),"ghost.gif")
cloud1 = Image(Point(width-300, 80), "cloud.gif")
cloud2 = Image(Point(width-50, 150), "cloud.gif")
cloud3 = Image(Point(width-250, 280), "cloud.gif")
bats = Image(Point(width-100, 350), "bats.gif")
castle = Image(Point(100, height-200), "castle.gif")
winghost = Image(Point(width/2, height/2-100), "winghost.gif")
loseghost = Image(Point(width/2, height/2-100), "loseghost.gif")
logo = Image(Point(width/2, height/2+30), "logo.gif")
introt1 = Text(Point(width/2, height/2-130), "Welcome to")
introt2 = Text(Point(width/2, height/2 + 170), "(aka the worst game ever I'm sorry)")
introt3 = Text(Point(width/2, height/2 + 220), "Click to begin")
introt1.setFace("helvetica")
introt2.setFace("helvetica")
introt2.setSize(10)
introt3.setSize(20)
introt3.setFace("helvetica")
introt1.setFill("white")
introt2.setFill("white")
introt3.setFill("white")

#logo.rs(2)
bats.rs(2)
cloud2.rs(3)
cloud3.rs(2)
ghost.rs(3)
winghost.rs(3)
loseghost.rs(3)
life1 = Image(Point(80 + 30, height-20), "skull.gif")
life2 = Image(Point(80 + 60, height-20), "skull.gif")
life3 = Image(Point(80 + 90, height-20), "skull.gif")
life1.rs(3)
life2.rs(3)
life3.rs(3)
moon.draw(window)
cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
castle.draw(window)
bats.draw(window)
ghost.draw(window)
logo.draw(window)
introt1.draw(window)
introt2.draw(window)
introt3.draw(window)
window.getMouse()
logo.undraw()
introt1.undraw()
introt2.undraw()
introt3.undraw()

life1.draw(window)
life2.draw(window)
life3.draw(window)

def newPumpkin():
    score = numbers[currentEntry]
    global no
    no = Text(Point(width-50, height-70), str(currentEntry + 1) + "/" +  str(len(numbers)))
    no.setFill("white")
    no.setFace('helvetica')
    global scoredis
    scoredis = Text(Point(width-50, height-20), score)
    scoredis.setFill("white")
    scoredis.setFace('helvetica')
    scale = -int(score[0]) +10
    global currentX
    currentX = randint(80, width-80)
    global pumpkin
    pumpkin = Image(Point(currentX, -10), "pumpkin.gif")
    pumpkin.rs(scale)
    pumpkin.draw(window)
    global gameScoreT
    gameScoreT = Text(Point(50, height-70), "Score: " + str(gameScore))
    gameScoreT.setFill("white")
    gameScoreT.setFace('helvetica')
    global lives
    lives = Text(Point(30, height-20), "Lives: ")
    lives.setFill("white")
    lives.setFace('helvetica')
    lives.draw(window)
    gameScoreT.draw(window)
    scoredis.draw(window)
    no.draw(window)

newPumpkin()

def finish():
    ghost.undraw()
    lives.undraw()
    resdis = Text(Point(width/2, height/2), "You " + str(result) + "!")
    cte = Text(Point(width/2, height/2 + 40), "Click to exit")
    sc = Text(Point(width/2, height/2 + 80), "Score: " + str(gameScore))
    resdis.setSize(20)
    resdis.setFill("white")
    resdis.setFace('helvetica')
    cte.setFill("white")
    cte.setFace('helvetica')
    sc.setFill("white")
    sc.setFace('helvetica')
    resdis.draw(window)
    cte.draw(window)
    sc.draw(window)
    if result == "win": winghost.draw(window)
    elif result == "lose": loseghost.draw(window)
    window.getMouse()
    window.close()
    

while play == True:
    keystr = window.checkKey()
    ghostPos = ghost.getAnchor()
    if(keystr == 'Right' and ghostPos.x < width-20):
        ghost.move(5, 0)
    if(keystr == 'Left' and ghostPos.x > 20):
        ghost.move(-5, 0)
        
    pos = pumpkin.getAnchor()
    puwid = pumpkin.getWidth()
    puhei = pumpkin.getHeight()
    if(pos.y >= height+100):
        currentEntry+=1
        pumpkin.undraw()
        scoredis.undraw()
        no.undraw()
        gameScore+=1
        gameScoreT.undraw()
        if(currentEntry == len(numbers)):
            play = False
            finish()
        else:
            newPumpkin()
    else:
        pumpkin.move(0, 0.2)
        if(pos.y + (puhei/2) + 10 > height-90):
            if(pos.x < ghostPos.x+(puwid/2) + 10 and pos.x > ghostPos.x-(puwid/2)-10):
                pumpkin.undraw()
                scoredis.undraw()
                no.undraw()
                gameScoreT.undraw()
                currentLives-=1
                if(currentLives == 2):
                    life3.undraw()
                elif(currentLives == 1):
                    life2.undraw()
                elif(currentLives == 0):
                    life1.undraw()
                    play = False
                    result = "lose"
                    finish()
                currentEntry+=1
                update()
                newPumpkin()
                
        