from cmu_graphics import *
from PIL import Image
import os
import time

def drawStartScreen(app):
    drawImage(app.startScreenImg, 0, 0)
    drawImage(app.gameLogoImg, app.width / 2, app.height / 6, align = 'center')
    drawImage(app.playButtonImg, app.width / 2, app.height - 50, align = 'center')

def mouseInPlayButton(app, mouseX, mouseY):
    width = 200 # button image is 200x100
    height = 100

    left = app.width / 2 - width / 2
    right = app.width / 2 + width / 2
    top = (app.height - 50) - height / 2
    bot = (app.height - 50) + height / 2

    if (left <= mouseX <= right) and (top <= mouseY <= bot):
        return True
    return False