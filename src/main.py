from cmu_graphics import *
from board import *
from zombies import *
from plants import *

def onAppStart(app):
    app.width = 1200
    app.height = 700
    boardVariables()

#     # continuously update list of currplants, include positions and type
#     # update panda positions

# create grid
def redrawAll(app):
    # drawRect(0, 0, 10, 10, fill='black')  # background
    drawBoard(app)
    drawBoardBorder(app)
    # make function for create checkerboard grid
        # for row in range step 2
        # for col in range step 2 start at 1
        # render images of each grid box, diff colors
    
    # for plant in plantslist
        # make function for drawing each plant

def main():
    runApp()
main()