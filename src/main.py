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
    app.stepsPerSecond = 20
    zombieVariables()

    # plants
    plantVariables()
    app.plantsList.append(PeaShooter(150, 125))
    app.plantsList.append(PeaShooter(150, 225))
    app.plantsList.append(PeaShooter(150, 325))
    app.plantsList.append(PeaShooter(150, 425))
    app.plantsList.append(PeaShooter(150, 525))
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
        drawPeas(app)
    
    # for plant in plantslist
        # make function for drawing each plant

def onStep(app):
    for plant in app.plantsList:
        if isinstance(plant, PeaShooter):
            plant.update(app)  # Peashooters shoot peas at intervals
    
    # Move all peas and check for collisions with zombies
    for pea in app.peasList:
        pea.move()  # Move the pea to the right
        for zombie in app.zombiesList:
            if pea.checkCollision(zombie):
                zombie.takeDamage(10)  # Decrease zombie health by 10 on collision
                app.peasList.remove(pea)  # Remove pea after collision
                break  # Stop checking other zombies once the pea hits one

    app.timeSinceLastZombie += 1 / app.stepsPerSecond

    if app.timeSinceLastZombie >= 20:
        app.timeSinceLastZombie = 0
        spawnZombie(app)
    
    for zombie in app.zombiesList:
        zombie.takeStep()

def main():
    runApp()
main()