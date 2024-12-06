from cmu_graphics import *
from PIL import Image
import os

def loadImages():
    sunImg = Image.open(os.path.join('src/images', 'sun_icon.png'))
    sunImg = sunImg.resize((80, 80))
    app.sunbarImg = CMUImage(sunImg)

    sunImg = sunImg.resize((40, 40))
    app.sunImg = CMUImage(sunImg)

    zombieImg = Image.open(os.path.join('src/images', 'generic_zombie.png'))
    zombieImg = zombieImg.resize((100, 100))
    app.zombieImg = CMUImage(zombieImg)

    peaImg = Image.open(os.path.join('src/images', f'pea.png'))
    peaImg = peaImg.resize((40, 40))
    app.peaImg = CMUImage(peaImg)

    peashooterImg = Image.open(os.path.join('src/images', 'peashooter.png'))
    peashooterImg = peashooterImg.resize((100, 100))
    app.peashooterImg = CMUImage(peashooterImg)


    sunflowerImg = Image.open(os.path.join('src/images', 'sunflower.png'))
    sunflowerImg = sunflowerImg.resize((100, 100))
    app.sunflowerImg = CMUImage(sunflowerImg)

    puffshroomImg = Image.open(os.path.join('src/images', 'puffshroom.png'))
    puffshroomImg = puffshroomImg.resize((100, 100))
    app.puffshroomImg = CMUImage(puffshroomImg)

    cabbageImg = Image.open(os.path.join('src/images', 'cabbage.png'))
    cabbageImg = cabbageImg.resize((100, 100))
    app.cabbageImg = CMUImage(cabbageImg)

    cabbageImg2 = Image.open(os.path.join('src/images', 'cabbage2.png'))
    cabbageImg2 = cabbageImg2.resize((100, 100))
    app.cabbageImg2 = CMUImage(cabbageImg2)

    sporeImg = Image.open(os.path.join('src/images', 'spores.png'))
    sporeImg = sporeImg.resize((40, 40))
    app.sporeImg = CMUImage(sporeImg)

    cabbageBallImg = Image.open(os.path.join('src/images', 'cabbage_ball.png'))
    cabbageBallImg = cabbageBallImg.resize((40, 40))
    app.cabbageBallImg = CMUImage(cabbageBallImg)
 
    messageImg = Image.open(os.path.join('src/images', 'message_paper.png'))
    messageImg = messageImg.resize((400, 400))
    app.messageImg = CMUImage(messageImg)

    startScreenImg = Image.open(os.path.join('src/images', 'start_screen.png'))
    startScreenImg = startScreenImg.resize((app.width, app.height))
    app.startScreenImg = CMUImage(startScreenImg)

    playButtonImg = Image.open(os.path.join('src/images', 'start_button.png'))
    playButtonImg = playButtonImg.resize((200, 100))
    app.playButtonImg = CMUImage(playButtonImg)

    gameLogoImg = Image.open(os.path.join('src/images', 'game_logo.png'))
    gameLogoImg = gameLogoImg.resize((400, 200))
    app.gameLogoImg = CMUImage(gameLogoImg)


def loadMenuImages():
    peashooterImg = Image.open(os.path.join('src/images', 'peashooter.png'))
    peashooterImg = peashooterImg.resize((60, 60))
    app.peashooterMenuImg = CMUImage(peashooterImg)


    sunflowerImg = Image.open(os.path.join('src/images', 'sunflower.png'))
    sunflowerImg = sunflowerImg.resize((60, 60))
    app.sunflowerMenuImg = CMUImage(sunflowerImg)

    puffshroomImg = Image.open(os.path.join('src/images', 'puffshroom.png'))
    puffshroomImg = puffshroomImg.resize((60, 60))
    app.puffshroomMenuImg = CMUImage(puffshroomImg)

    cabbageImg = Image.open(os.path.join('src/images', 'cabbage.png'))
    cabbageImg = cabbageImg.resize((80, 80))
    app.cabbageMenuImg = CMUImage(cabbageImg)