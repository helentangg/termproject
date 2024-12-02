from cmu_graphics import *
from PIL import Image
import os

from board import *
from zombies import *
from plants import *
from load_images import *

def onAppStart(app):
    # game
    app.gameOver = False
    app.stepsPerSecond = 1000
    loadImages()

    # user interactions
    app.cursorLocation = None
    app.plantCardLocation = None
    app.selectedPlantCard = None

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
        drawMenu(app)
        drawSunbar(app)
        drawZombie(app)
        drawPlant(app)
        drawPeas(app)

        if app.plantCardLocation != None and app.selectedPlantCard != None:
            plantImg = Image.open(os.path.join('src/images', f'{app.selectedPlantCard}.png'))
            plantImg = plantImg.resize((60, 60))
            plantImg = CMUImage(plantImg)
            x, y = app.plantCardLocation
            drawImage(plantImg, x, y, align = 'center')

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

# def onMouseMove(app, mouseX, mouseY):
#     app.cursorLocation = (mouseX, mouseY)

def onMousePress(app, mouseX, mouseY):
    if mouseInCard(app, mouseX, mouseY) != None:
        cardNum = mouseInCard(app, mouseX, mouseY) # getting which card the mouse is in
        app.selectedPlantCard = app.plantCards[cardNum]
        app.plantCardLocation = (mouseX, mouseY)
        
        
    app.dotLocation = app.lineStartLocation = (mouseX, mouseY)
    app.lineEndLocation = None
    app.draggingLine = True

def onMouseDrag(app, mouseX, mouseY):
     app.plantCardLocation = (mouseX, mouseY)

# def onMouseRelease(app, mouseX, mouseY):
#     app.

def main():
    runApp()
main()