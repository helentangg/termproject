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
        super.__init__(x)
        super.__init__(y)

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

class Pea:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.step = 10 # moves 5 pixels every step

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

def drawPlant(app):
    for plant in app.plantsList:
        type = plant.type
        plantImg = Image.open(os.path.join('src/images', f'{type}.png'))
        plantImg = plantImg.resize((100, 100))
        cmuImage1 = CMUImage(plantImg)
        drawImage(cmuImage1, plant.x, plant.y, align='center')

def drawPeas(app):
    for pea in app.peasList:
        img = Image.open(os.path.join('src/images', f'pea.png'))
        img = img.resize((30, 30))
        cmuImage1 = CMUImage(img)
        drawImage(cmuImage1, pea.x, pea.y, align='center')

def getRow(y):
    return y // 100
