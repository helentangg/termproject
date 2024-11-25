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
        self.shootingInterval = 30  # Peashooter shoots a pea every 30 steps
        self.timeSinceLastShot = 0
    
    def shoot(self, app):
        newPea = Pea(self.x, self.y)  # Pea starts at the Peashooter's position
        app.peasList.append(newPea)  # Add the new Pea to the peasList
    
    def update(self, app):
        # Handle the Peashooter's shooting logic (shoots every 30 steps)
        self.timeSinceLastShot += 1
        if self.timeSinceLastShot >= self.shootingInterval:
            self.shoot(app)  # Call shoot method to create and add new Pea to the list
            self.timeSinceLastShot = 0  # Reset the shooting interval

class Pea:
    def __init__(self, x, y):
        self.x = x  # Initial x position of the pea
        self.y = y  # y position (same as the Peashooter)
        self.width = 10  # Width of the pea
        self.height = 10  # Height of the pea
        self.speed = 5  # Speed of the pea (moves horizontally)

    def move(self):
        self.x += self.speed  # Move the pea to the right

    def checkCollision(self, zombie):
        # Check if the pea collides with a zombie
        if self.x < zombie.x + 100 and self.x + 100 > zombie.x and \
           self.y < zombie.y + 100 and self.y + 100 > zombie.y:
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
        drawRect(pea.x, pea.y, pea.width, pea.height, fill='green')