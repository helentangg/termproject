from cmu_graphics import *
from PIL import Image
import os

from board import *
from zombies import *
from plants import *

def onAppStart(app):
    app.width = 1200
    app.height = 700
    app.stepsPerSecond = 20
    boardVariables()
    zombieVariables()

#     # continuously update list of currplants, include positions and type
#     # update panda positions

# create grid
def redrawAll(app):
    # drawRect(0, 0, 10, 10, fill='black')  # background
    drawBoard(app)
    # drawBoardBorder(app)
    # drawMenu(app)
    drawZombie(app)
    
    # for plant in plantslist
        # make function for drawing each plant

def onStep(app):
    while len(app.zombiesList) < 3:
        spawnZombie(app)

def main():
    runApp()
main()