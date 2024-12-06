from cmu_graphics import *
from PIL import Image
import os

from board import *
from zombies import *
from plants import *
from load_images import *
from start_screens import *

def onAppStart(app):
    # game
    app.width = 1200
    app.height = 700
    app.gameOver = False
    app.stepsPerSecond = 30
    loadImages()
    loadMenuImages()

    # screens
    app.startScreen = True

    # user interactions
    app.plantCardLocation = None
    app.selectedPlantCard = None
    app.cardNum = None

    # board
    boardVariables()

    # zombie
    zombieVariables()

    # plants
    plantVariables()

# create grid
def redrawAll(app):
    if app.startScreen == True:
        drawStartScreen(app)

    if app.gameOver == False and app.startScreen == False:
        drawBoard(app)
        drawMenu(app)
        drawSunbar(app)
        drawPlant(app)
        drawZombie(app)
        drawPeas(app)
        drawSpores(app)
        drawSun(app)

        if app.plantCardLocation != None and app.selectedPlantCard != None:
            plantImg = Image.open(os.path.join('src/images', f'{app.selectedPlantCard}.png'))
            plantImg = plantImg.resize((60, 60))
            plantImg = CMUImage(plantImg)
            x, y = app.plantCardLocation
            drawImage(plantImg, x, y, align = 'center')
        
        if app.notEnoughSunMessage == True:
            centeredMessage(app, 'Not enough sun! \nPress c to continue')
        
        if app.cantPlaceThereMessage:
            centeredMessage(app, "Can't place there! \nPress c to continue")

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
    
    for sun in app.sunList:
        sun.move()
    
    app.timeSinceLastZombie += 1

    if app.timeSinceLastZombie >= app.stepsPerSecond * 10:
        app.timeSinceLastZombie = 0
        spawnZombie(app)
    
    for zombie in app.zombiesList:
        zombie.takeStep()

        for plant in app.plantsList:
            zombie.eat(plant)
        

def onMousePress(app, mouseX, mouseY):
    if app.startScreen == True:
        if mouseInPlayButton(app, mouseX, mouseY):
            app.startScreen = False
    
    if mouseInCard(app, mouseX, mouseY) != None:
        app.cardNum = mouseInCard(app, mouseX, mouseY) # getting which card the mouse is in
        app.selectedPlantCard = app.plantCards[app.cardNum]
        app.plantCardLocation = (mouseX, mouseY)

    for sun in app.sunList:
        if sun.mouseInSun(mouseX, mouseY):
            app.sunList.remove(sun)
            app.sunCount += 100
            break

def onMouseDrag(app, mouseX, mouseY):
     app.plantCardLocation = (mouseX, mouseY)

def onMouseRelease(app, mouseX, mouseY):
    app.plantCardLocation = None
    plantIndex = None
    for i in range(len(app.plantCards)):
        if app.plantCards[i] == app.selectedPlantCard:
            plantIndex = i
            break
    
    if app.cardNum != None:
        if enoughSun(plantIndex) == True:
            row = getRow(mouseY)
            col = getCol(mouseX)
            if 1 <= row <= 5 and 1 <= col <= 9:
                cantPlace = False
                for plant in app.plantsList:
                    if isinstance(plant, Plant) and (plant.x == col * 100 + 50 and plant.y == row * 100 + 25):
                        cantPlace = True
                        break
                
                if cantPlace == False:
                    plantType = app.selectedPlantCard
                    if plantType == 'peashooter':
                        app.plantsList.append(PeaShooter(col * 100 + 50, row * 100 + 25))
                        app.sunCount -= 150
                    
                    elif plantType == 'sunflower':
                        app.plantsList.append(Sunflower(col * 100 + 50, row * 100 + 25))
                        app.sunCount -= 125

                    elif plantType == 'puffshroom':
                        app.plantsList.append(Puffshroom(col * 100 + 50, row * 100 + 25))
                        app.sunCount -= 300

                    elif plantType == 'cabbage':
                        app.plantsList.append(Cabbage(col * 100 + 50, row * 100 + 25))
                        app.sunCount -= 1500
                else:
                    app.cantPlaceThereMessage = True
            app.cardNum = None
        else:
            app.notEnoughSunMessage = True
            app.cardNum = None

    app.selectedPlantCard = None

def onKeyPress(app, key):
    if key == 'c' and (app.notEnoughSunMessage or app.cantPlaceThereMessage):
        app.notEnoughSunMessage = False
        app.cantPlaceThereMessage = False

def main():
    runApp()
main()