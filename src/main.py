from cmu_graphics import *
from PIL import Image
import os

from board import *
from zombies import *
from plants import *

def onAppStart(app):
    # game
    app.gameOver = False
    app.stepsPerSecond = 100

    # board
    app.width = 1200
    app.height = 700
    boardVariables()

    # zombie
    zombieVariables()

    # plants
    plantVariables()
    app.plantsList.append(PeaShooter(150, 125))
    app.plantsList.append(PeaShooter(150, 225))
    app.plantsList.append(PeaShooter(150, 325))
    app.plantsList.append(PeaShooter(150, 425))
    app.plantsList.append(PeaShooter(150, 525))

# create grid
def redrawAll(app):
    if app.gameOver == False:
        drawBoard(app)
        drawMenu(app) # still working on this function
        drawZombie(app)
        drawPlant(app)
        drawPeas(app)

def onStep(app):
    for plant in app.plantsList:
        if isinstance(plant, PeaShooter):
            plant.update(app)

    for pea in app.peasList:
        pea.move()
        for zombie in app.zombiesList:
            if pea.hit(zombie):
                zombie.takeDamage(20)
                app.peasList.remove(pea)
                break

    app.timeSinceLastZombie += app.stepsPerSecond

    if app.timeSinceLastZombie >= app.stepsPerSecond * 50:
        app.timeSinceLastZombie = 0
        spawnZombie(app)
    
    for zombie in app.zombiesList:
        zombie.takeStep()

def main():
    runApp()
main()