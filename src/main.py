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
    app.stepsPerSecond = 30
    loadImages()
    loadMenuImages()

    # user interactions
    app.cursorLocation = None
    app.plantCardLocation = None
    app.selectedPlantCard = None
    app.cardNum = None

    # board
    app.width = 1200
    app.height = 700
    boardVariables()

    # zombie
    zombieVariables()

    # plants
    plantVariables()

# create grid
def redrawAll(app):
    if app.gameOver == False:
        drawBoard(app)
        drawMenu(app)
        drawSunbar(app)
        drawZombie(app)
        drawPlant(app)
        drawPeas(app)
        drawSpores(app)

        if app.plantCardLocation != None and app.selectedPlantCard != None:
            plantImg = Image.open(os.path.join('src/images', f'{app.selectedPlantCard}.png'))
            plantImg = plantImg.resize((60, 60))
            plantImg = CMUImage(plantImg)
            x, y = app.plantCardLocation
            drawImage(plantImg, x, y, align = 'center')

def onStep(app):
    for plant in app.plantsList:
        if isinstance(plant, Plant):
            plant.update(app)

    for pea in app.peasList:
        pea.move()
        for zombie in app.zombiesList:
            if pea.hit(zombie):
                zombie.takeDamage(20)
                app.peasList.remove(pea)
                break
    
    for spore in app.sporesList:
        spore.move()
        for zombie in app.zombiesList:
            if spore.hit(zombie):
                zombie.takeDamage(10)
                app.sporesList.remove(spore)
                break

    app.timeSinceLastZombie += 1

    if app.timeSinceLastZombie >= app.stepsPerSecond * 10:
        app.timeSinceLastZombie = 0
        spawnZombie(app)
    
    for zombie in app.zombiesList:
        zombie.takeStep()

# def onMouseMove(app, mouseX, mouseY):
#     app.cursorLocation = (mouseX, mouseY)

def onMousePress(app, mouseX, mouseY):
    if mouseInCard(app, mouseX, mouseY) != None:
        app.cardNum = mouseInCard(app, mouseX, mouseY) # getting which card the mouse is in
        app.selectedPlantCard = app.plantCards[app.cardNum]
        app.plantCardLocation = (mouseX, mouseY)

def onMouseDrag(app, mouseX, mouseY):
     app.plantCardLocation = (mouseX, mouseY)

def onMouseRelease(app, mouseX, mouseY):
    app.plantCardLocation = None
    if app.cardNum != None:
        row = getRow(mouseY)
        col = getCol(mouseX)
        if 1 <= row <= 5 and 1 <= col <= 9:
            plantType = app.selectedPlantCard
            if plantType == 'peashooter':
                app.plantsList.append(PeaShooter(col * 100 + 50, row * 100 + 25))
            
            elif plantType == 'sunflower':
                app.plantsList.append(Sunflower(col * 100 + 50, row * 100 + 25))

            elif plantType == 'puffshroom':
                app.plantsList.append(Puffshroom(col * 100 + 50, row * 100 + 25))

            elif plantType == 'cabbage':
                app.plantsList.append(Cabbage(col * 100 + 50, row * 100 + 25))
    app.selectedPlantCard = None
            
def main():
    runApp()
main()