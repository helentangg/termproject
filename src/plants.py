from cmu_graphics import *
import random
from PIL import Image
import os

class Plant:
    def __init__(self, x, y):
        self.type = type
        self.x = x
        self.y = y

# sunflower: produces sun for the user to buy additional plants
class Sunflower(Plant):
    def __init__(self, x, y):
        self.type = 'sunflower'
        self.x = x
        self.y = y

# peashooter: shoots peas in a straight line at zombie, deals 20 damage
class PeaShooter(Plant):
    def __init__(self, x, y):
        self.type = 'peashooter'
        self.x = x
        self.y = y
        self.shootingInterval = 30  # shoots pea every 30 steps
        self.timeSinceLastShot = 0
    
    def shoot(self, app):
        newPea = Pea(self.x, self.y) # create new pea at peashooters position
        app.peasList.append(newPea)
    
    def update(self, app):
        zombiePresent = False
        for zombie in app.zombiesList:
            if getRow(zombie.y) == getRow(self.y):
                zombiePresent = True
                break
        
        # only shoot if there is a zombie in the row
        if zombiePresent:
            self.timeSinceLastShot += 1
            if self.timeSinceLastShot >= self.shootingInterval:
                self.shoot(app) 
                self.timeSinceLastShot = 0 

class Puffshroom(Plant):
    def __init__(self, x, y):
        self.type = 'puffshroom'
        self.x = x
        self.y = y
        self.shootingInterval = 20
        self.timeSinceLastShot = 0

    def shoot(self, app):
        newSpore = Spore(self.x, self.y) # create new pea at peashooters position
        app.sporesList.append(newSpore)
    
    def update(self, app):
        zombiePresent = False
        for zombie in app.zombiesList:
            if getRow(zombie.y) == getRow(self.y):
                zombiePresent = True
                break
        
        # only shoot if there is a zombie in the row
        if zombiePresent:
            self.timeSinceLastShot += 1
            if self.timeSinceLastShot >= self.shootingInterval:
                self.shoot(app) 
                self.timeSinceLastShot = 0 

class Cabbage(Plant):
    def __init__(self, x, y):
        self.type = 'cabbage'
        self.x = x
        self.y = y

class Pea:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.step = 10 # moves 10 pixels every step

    def move(self):
        self.x += self.step

    def hit(self, zombie):
        # if pea lands within the zombie's hitbox
        if self.x < zombie.x + 50 and self.x > zombie.x - 50 and \
           self.y < zombie.y + 50 and self.y > zombie.y - 50:
            return True
        return False

class Spore:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.step = 10 # moves 10 pixels every step

    def move(self):
        self.x += self.step

    def hit(self, zombie):
        # if pea lands within the zombie's hitbox
        if self.x < zombie.x + 50 and self.x > zombie.x - 50 and \
           self.y < zombie.y + 50 and self.y > zombie.y - 50:
            return True
        return False
    
def plantVariables():
    app.plantsList = []
    app.peasList = []
    app.sporesList = []

def drawPlant(app):
    for plant in app.plantsList:
        type = plant.type
        if type == 'peashooter':
            drawImage(app.peashooterImg, plant.x, plant.y, align='center')
        elif type == 'sunflower':
            drawImage(app.sunflowerImg, plant.x, plant.y, align='center')
        elif type == 'puffshroom':
            drawImage(app.puffshroomImg, plant.x, plant.y, align='center')
        elif type == 'cabbage':
            drawImage(app.cabbageImg, plant.x, plant.y, align='center')

def drawPeas(app):
    for pea in app.peasList:
        drawImage(app.peaImg, pea.x, pea.y, align='center')

def drawSpores(app):
    for spore in app.sporesList:
        drawImage(app.sporeImg, spore.x, spore.y, align='center')

def getRow(y):
    return y // 100
