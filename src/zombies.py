from cmu_graphics import *
import random
from PIL import Image
import os

class Zombie():
    def __init__(self, x, y):
        # self.type = type -- can potentially add diff panda types
        self.x = x
        self.y = y
        self.health = 100

    def takeStep(self):
        self.x -= 1
        if self.x <= 100:
            app.gameOver = True
    
    def takeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        print("Zombie is dead!")
        app.zombiesList.remove(self)

def zombieVariables():
    app.zombiesList = []
    app.timeSinceLastZombie = 0

def generateRandomStartingPos(app):
    row = random.randint(0, 4)
    col = 9
    x = col * 100 + 150 # cells are 100x100, adding 150 centers the image
    y = row * 100 + 150
    return (x, y)
    
def drawZombie(app):
    for zombie in app.zombiesList:
        zombieImg = Image.open(os.path.join('src/images', 'generic_zombie.png'))
        zombieImg = zombieImg.resize((100, 100))
        cmuImage1 = CMUImage(zombieImg)
        drawImage(cmuImage1, zombie.x, zombie.y, align='center')

def spawnZombie(app):
    x, y = generateRandomStartingPos(app)
    newZombie = Zombie(x, y)
    app.zombiesList.append(newZombie)

    
