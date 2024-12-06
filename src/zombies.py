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

# class GenericZombie(Zombie):
#     def __init__(self, x, y, health):
#         self.x = x
#         self.y = y
#         self.health = 100

# class ConeZombie(Zombie):
#     def __init__(self, x, y, health):
#         self.x = x
#         self.y = y
#         self.health = 200

# class SmartZombie(Zombie):
#     def __init__(self, x, y, health):
#         self.x = x
#         self.y = y
#         self.health = 100

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
        drawImage(app.zombieImg, zombie.x, zombie.y, align='center')

def spawnZombie(app):
    x, y = generateRandomStartingPos(app)
    newZombie = Zombie(x, y)
    app.zombiesList.append(newZombie)

    
