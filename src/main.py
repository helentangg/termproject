from cmu_graphics import *
from PIL import Image
import os, pathlib

from board import *
from zombies import *
from plants import *
from load_images import *
from menu_screens import *

def onAppStart(app):
    # game
    app.width = 1200
    app.height = 700
    app.gameOver = False
    app.gameLost = False
    app.stepsPerSecond = 30
    app.gameStart = False
    loadImages()
    loadMenuImages()

    # waves variables
    app.currentWave = 1
    app.waveZombieCount = 0
    app.maxZombieCount = 5
    app.timeSinceWaveStart = 0
    app.timeBetweenWaves = 300
    app.timeUntilNextWave = 0
    app.maxWave = False

    app.instructions = False

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

    # sound
    app.gamesound = loadSound('src/game_backgroundsound.mp3')
    app.lostsound = loadSound('src/lostsound.mp3')
    app.lostsoundplayed = False

# create grid
def redrawAll(app):
    if app.startScreen == True:
        app.gamesound.play(restart=True)
        drawStartScreen(app)

        if app.instructions:
            instructionsMsg(app, "GAME RULES: \nUse the plants to battle the zombies! \nThere are 4 types of plants: sunflower (spawns sun), \npeashooter ," +
                            "puffshroom, and smart cabbage (shoots at \nthe strongest zombie on the screen) \nThere are 3 types of zombies: generic, cone (has double the health) \nand smart zombie (moves to rows with the least)"
                            + " number of plants \nUse the sun to buy plants and drag them onto the grid. \nZombies will spawn in 3 waves. Once the 3 waves are over \nyou win!"
                            + " If a zombie reaches the end of the grid, you lose")

    elif app.gameOver == False and app.startScreen == False and app.gameStart:
        drawImage(app.backImg, 0, 0)
        app.gamesound.play()
        drawBoard(app)
        drawWhitePieces(app)
        drawMenu(app)
        drawSunbar(app)
        drawWaveBar(app)
        waveLabel(app)
        drawPlant(app)
        drawZombie(app)
        drawPeas(app)
        drawSpores(app)
        drawSun(app)
        drawCabbageBall(app)

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
    
    elif app.gameOver and app.gameLost:
        if app.lostsoundplayed == False:
            app.lostsound.play()
        drawGameOverScreen(app)
    
    elif app.gameOver and app.gameLost == False:
        drawWinScreen(app)


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
    
    for ball in app.cabbageBallList:
        ball.move()
        for zombie in app.zombiesList:
            if ball.hit(zombie):
                zombie.takeDamage(20)
                app.cabbageBallList.remove(ball)
                break

    app.timeCount = 0

    app.timeSinceWaveStart += 1
    app.timeSinceLastZombie += 1
    if app.maxWave:
        if app.zombiesList == []:
            app.gameOver = True
            app.gameLost = False
    else:
        # spawning zombies while count is less than or equal to max for the wave, zombies spawn in faster each wave
        if app.waveZombieCount < app.maxZombieCount and app.timeSinceLastZombie >= app.stepsPerSecond * (12//app.currentWave):
            app.timeSinceLastZombie = 0
            spawnZombie(app)
            app.waveZombieCount += 1

        if app.waveZombieCount >= app.maxZombieCount:
            # this logic referenced from chatGPT
            if app.timeSinceLastZombie >= app.timeBetweenWaves:
                if app.currentWave < 3:
                    app.currentWave += 1
                    app.maxZombieCount *= app.currentWave
                    app.waveZombieCount = 0
                    app.timeSinceLastZombie = 0
                    app.timeSinceWaveStart = 0
                else:
                    app.maxWave = True
    
    for zombie in app.zombiesList:
        zombie.takeStep()

        for plant in app.plantsList:
            zombie.eat(plant)
        

def onMousePress(app, mouseX, mouseY):
    if app.startScreen == True:
        if app.gameOver == True:
            if mouseInPlayButton(app, mouseX, mouseY):
                resetGame(app)
                app.gameStart = True
        else:
            if mouseInPlayButton(app, mouseX, mouseY):
                app.startScreen = False
                app.gameStart = True
            
            if mouseInInfoButton(app, mouseX, mouseY):
                app.instructions = not app.instructions
        
    if app.gameOver == True and app.gameLost:
        if mouseInMenuButton(app, mouseX, mouseY):
            app.startScreen = True
    
    if app.gameOver and app.gameLost == False:
        if mouseInMenuButton(app, mouseX, mouseY):
            app.startScreen = True

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

def resetGame(app):
    app.plantsList = []
    app.peasList = []
    app.sporesList = []
    app.sunList = []
    app.zombiesList = []
    app.sunCount = 300
    app.timeSinceLastZombie = 0
    app.cabbageBallList = []
    app.notEnoughSunMessage = False
    app.cantPlaceThereMessage = False
    app.gameOver = False
    app.gameLost = False
    app.currentWave = 1
    app.waveZombieCount = 0
    app.maxZombieCount = 1
    app.timeSinceWaveStart = 0
    app.timeBetweenWaves = 300
    app.timeUntilNextWave = 0
    app.maxWave = False
    app.lostsoundplayed = False
    app.instructions = False

def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)

def main():
    runApp()
main()