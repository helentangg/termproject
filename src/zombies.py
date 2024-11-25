from cmu_graphics import *
import random
from PIL import Image
import os

class Zombie():
    def __init__(self, x, y):
        # self.type = type -- can potentially add diff panda types
        self.posX = x
        self.posY = y

def zombieVariables():
    app.zombiesList = []

def generateRandomStartingPos(app):
    row = random.randint(0, 5)
    col = 9
    x = col * 100 + 150 # cells are 100x100, adding 150 centers the image
    y = row * 100 + 50
    return (x, y)
    
def drawZombie(app):
    for zombie in app.zombiesList:
        zombieImg = Image.open(os.path.join('src/images', 'generic_zombie.png'))
        zombieImg = zombieImg.resize((100, 100))
        cmuImage1 = CMUImage(zombieImg)
        drawImage(cmuImage1, zombie.posX, zombie.posY, align='center')

def spawnZombie(app):
    x, y = generateRandomStartingPos(app)
    newZombie = Zombie(x, y)
    app.zombiesList.append(newZombie)

    
