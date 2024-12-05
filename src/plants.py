from cmu_graphics import *
import random
from PIL import Image
import os
import math

class Plant:
    def __init__(self, x, y):
        self.type = type
        self.x = x
        self.y = y

# sunflower: produces sun for the user to buy additional plants, cost: 125 sun
class Sunflower(Plant):
    def __init__(self, x, y):
        self.type = 'sunflower'
        self.x = x
        self.y = y
        self.timeSinceLastSun = 0
        self.sunSpawnInterval = 240
    
    def sunSpawn(self):
        targetX, targetY = randomSunSpawnLocation(self)
        newSun = Sun(self.x, self.y, targetX, targetY)
        app.sunList.append(newSun)

    def update(self, app):
        self.timeSinceLastSun += 1
        if self.timeSinceLastSun >= self.sunSpawnInterval:
            self.sunSpawn()
            self.timeSinceLastSun = 0
        
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

class Sun:
    def __init__(self, x, y, targetX, targetY):
        self.x = x
        self.y = y
        self.targetX = targetX 
        self.targetY = targetY
        self.step = 1
        self.moving = True

    # movement code referenced from: https://github.com/nealholt/python_programming_curricula/blob/master/CS1/0550_galaga/pygame_galaga2_shoot_any_direction.py
    def move(self):
        if self.moving:
            angle = math.atan2(self.y - self.targetY, self.x - self.targetX) # angle from target to sunflower
            # distance = math.dist((self.targetX, self.targetY), (self.x, self.y))

            if self.x == self.targetX and self.y == self.targetY:
                self.moving = False

            else:
                self.x -= math.cos(angle) * self.step
                self.y -= math.sin(angle) * self.step
    
    def mouseInSun(self, mouseX, mouseY):
        radius = 20 # sun image was scaled to 40x40
        if math.dist((self.x, self.y), (mouseX, mouseY)) <= radius:
            return True
        return False

def plantVariables():
    app.plantsList = []
    app.peasList = []
    app.sporesList = []
    app.sunList = []

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

def drawSun(app):
    for sun in app.sunList:
        drawImage(app.sunImg, sun.x, sun.y, align = 'center')

def getRow(y):
    return y // 100

# spawn sun in 1.5 cell radius to sunflower
def randomSunSpawnLocation(self):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)

    x += self.x
    y += self.x

    if x < 150:
        x = 150
    if y < 150:
        y = 150
    
    return (x, y) 