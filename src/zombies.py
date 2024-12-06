from cmu_graphics import *
import random
from PIL import Image
import os

class Zombie():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.eating = False

    def takeStep(self):
        self.inPlantSquare(app)
        if self.eating == False:
            self.x -= 1
            if self.x <= 100:
                app.gameOver = True
    
    def takeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()
        
    def inPlantSquare(self, app):
        self.eating = False
        for plant in app.plantsList:
            if self.x == plant.x + 30 and self.y == plant.y:
                self.eating = True
                break

    def die(self):
        app.zombiesList.remove(self)

    def eat(self, plant):
        if self.x == plant.x + 30 and self.y == plant.y:
            plant.takeDamage(0.5)

class GenericZombie(Zombie):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

class ConeZombie(Zombie):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 200

class SmartZombie(Zombie):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
    
    def takeStep(self):
        allRows = [0, 0, 0, 0, 0]

        for plant in app.plantsList:
            row = getRow(plant.y) - 1
            allRows[row] += 1
        
        targetRows = []
        minNum = min(allRows) # from chatGPT
        for i in range(len(allRows)):
            if allRows[i] == minNum:
                targetRows.append(i)
        
        self.inPlantSquare(app)
        if self.eating == False:
            # zombie should stay in its own row if its the minNum, even if other rows are also
            zombieRow = getRow(self.y) - 1
            closestRow = None
            smallestDiff = 5
            for row in targetRows:
                if abs(row - zombieRow) <= smallestDiff:
                    smallestDiff = abs(row - zombieRow)
                    closestRow = row

            if self.y < closestRow * 100 + 125:
                self.y += 1
            elif self.y > closestRow * 100 + 125:
                self.y -= 1

            if self.y == closestRow * 100 + 125:
                self.x -= 1
                if self.x <= 100:
                    app.gameOver = True
                    app.gameLost = True

def zombieVariables():
    app.zombiesList = []
    app.timeSinceLastZombie = 0

def generateRandomStartingPos(app):
    row = random.randint(0, 4)
    col = 9
    x = col * 100 + 150 # cells are 100x100, adding 150 centers the image
    y = row * 100 + 125
    return (x, y)
    
def drawZombie(app):
    for zombie in app.zombiesList:
        if isinstance(zombie, GenericZombie):
            drawImage(app.zombieImg, zombie.x, zombie.y, align='center')
        elif isinstance(zombie, ConeZombie):
            drawImage(app.coneZombieImg, zombie.x, zombie.y, align='center')
        elif isinstance(zombie, SmartZombie):
            drawImage(app.smartZombieImg, zombie.x, zombie.y, align='center')

def spawnZombie(app):
    x, y = generateRandomStartingPos(app)
    randomType = random.randint(0, 2)
    if randomType == 0:
        newZombie = GenericZombie(x, y)
    elif randomType == 1:
        newZombie = ConeZombie(x, y)
    elif randomType == 2:
        newZombie = SmartZombie(x, y)
    app.zombiesList.append(newZombie)

def getRow(y):
    return y // 100

def getCol(x):
    return x // 100

    
