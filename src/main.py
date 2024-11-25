from cmu_graphics import *
from PIL import Image
import os

from board import *
from zombies import *
from plants import *

def onAppStart(app):
    # game
    app.gameOver = False

    # board
    app.width = 1200
    app.height = 700
    boardVariables()

    # zombie
    app.stepsPerSecond = 1
    zombieVariables()

    # plants
    plantVariables()
    app.plantsList.append(PeaShooter(150, 150))

#     # continuously update list of currplants, include positions and type
#     # update panda positions

# create grid
def redrawAll(app):
    if app.gameOver == False:
        # drawRect(0, 0, 10, 10, fill='black')  # background
        drawBoard(app)
        # drawMenu(app)
        drawZombie(app)
        drawPlant(app)
    
    # for plant in plantslist
        # make function for drawing each plant

def onStep(app):
    app.timeSinceLastZombie += 1 / app.stepsPerSecond

    if app.timeSinceLastZombie >= 20:
        app.timeSinceLastZombie = 0
        spawnZombie(app)
    
    for zombie in app.zombiesList:
        zombie.takeStep()

def main():
    runApp()
main()