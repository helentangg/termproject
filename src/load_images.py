from cmu_graphics import *
from PIL import Image
import os

def loadImages():
    sunImg = Image.open(os.path.join('src/images', 'sun_icon.png'))
    sunImg = sunImg.resize((80, 80))
    app.sunImg = CMUImage(sunImg)

    zombieImg = Image.open(os.path.join('src/images', 'generic_zombie.png'))
    zombieImg = zombieImg.resize((100, 100))
    app.zombieImg = CMUImage(zombieImg)

    peaImg = Image.open(os.path.join('src/images', f'pea.png'))
    peaImg = peaImg.resize((30, 30))
    app.peaImg = CMUImage(peaImg)

    plantImg = Image.open(os.path.join('src/images', 'peashooter.png'))
    plantImg = plantImg.resize((100, 100))
    app.peashooterImg = CMUImage(plantImg)