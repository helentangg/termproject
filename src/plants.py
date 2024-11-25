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

# peashooter: shoots peas in a straight line at zombie
class PeaShooter(Plant):
    def __init__(self, x, y):
        self.type = 'peashooter'
        self.x = x
        self.y = y

def plantVariables():
    app.plantsList = []

def drawPlant(app):
    for plant in app.plantsList:
        type = plant.type
        plantImg = Image.open(os.path.join('src/images', f'{type}.png'))
        plantImg = plantImg.resize((100, 100))
        cmuImage1 = CMUImage(plantImg)
        drawImage(cmuImage1, 150, 150, align='center')