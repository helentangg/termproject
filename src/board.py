from cmu_graphics import *
from PIL import Image
import os
import time

# put in onAppStart
def boardVariables():
    app.rows = 5
    app.cols = 10
    app.boardLeft = 100
    app.boardTop = 100
    app.boardWidth = 1000
    app.boardHeight = 500
    app.cellBorderWidth = 2
    app.menuWidth = 800
    app.menuHeight = 100
    app.sunbarWidth = 200
    app.sunbarHeight = 100
    app.sunCount = 150
    app.plantCards = ['sunflower', 'peashooter', 'puffshroom', 'cabbage']
    app.plantCardsSunValue = [125, 150, 300, 1500]
    app.notEnoughSunMessage = False
    app.cantPlaceThereMessage = False

def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border='black',
             borderWidth=app.cellBorderWidth)

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

def drawBoardBorder(app):
  # draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)
  
def drawBoard(app): # 5 x 9 board - 10 columns, one extra for zombie spawn
    for row in range(app.rows):
        for col in range(app.cols):
            if col == 9:
                color = 'saddleBrown'
            elif (col + row) % 2 == 0:
                color = 'green'
            else:
                color = 'lightGreen'
            drawCell(app, row, col, color)

def drawMenu(app):
    drawRect(app.boardLeft, 0, app.menuWidth, app.menuHeight, fill = 'grey', opacity = 50)

    # drawing all cards - cards are 180x80
    cellWidth, cellHeight = getCellSize(app)
    cardWidth = cellWidth * 2 - 20
    for i in range(len(app.plantCards)):
        drawCard(app, app.boardLeft + cardWidth*i + 10 + i*20, 10)
        if app.plantCards[i] == 'sunflower':
            drawImage(app.sunflowerMenuImg, app.boardLeft + cardWidth*i + 10 + 90 + i*20, 50, align = 'center')
            drawLabel('125', app.boardLeft + cardWidth*i + 10 + 90 + i*20 + 50, 50, align = 'center', size = 16)
        elif app.plantCards[i] == 'peashooter':
            drawImage(app.peashooterMenuImg, app.boardLeft + cardWidth*i + 10 + 90 + i*20, 50, align = 'center')
            drawLabel('150', app.boardLeft + cardWidth*i + 10 + 90 + i*20 + 50, 50, align = 'center', size = 16)
        elif app.plantCards[i] == 'puffshroom':
            drawImage(app.puffshroomMenuImg, app.boardLeft + cardWidth*i + 10 + 90 + i*20, 50, align = 'center')
            drawLabel('300', app.boardLeft + cardWidth*i + 10 + 90 + i*20 + 50, 50, align = 'center', size = 16)
        elif app.plantCards[i] == 'cabbage':
            drawImage(app.cabbageMenuImg, app.boardLeft + cardWidth*i + 10 + 90 + i*20, 50, align = 'center')
            drawLabel('1500', app.boardLeft + cardWidth*i + 10 + 90 + i*20 + 50, 50, align = 'center', size = 16)

def drawCard(app, x, y):
    cellWidth, cellHeight = getCellSize(app)
    cardWidth = cellWidth * 2 - 20
    cardHeight = cellHeight - 20
    drawRect(x, y, cardWidth, cardHeight, fill = 'white', opacity = 50, border = 'black')
    drawRect(x, y, cardWidth, cardHeight, fill = None, border = 'black')

def drawSunbar(app):
    drawRect(app.menuWidth + app.boardLeft, 0, app.sunbarWidth, app.sunbarHeight, fill = 'grey', opacity = 10)

    cellWidth, cellHeight = getCellSize(app)
    drawImage(app.sunbarImg, app.menuWidth + app.boardLeft + cellWidth + 10, 10)
    drawLabel(f'{app.sunCount}', app.menuWidth + app.boardLeft + cellWidth // 2, cellHeight // 2, size = 40)

def mouseInCard(app, mouseX, mouseY):
    cellWidth, cellHeight = getCellSize(app)
    cardWidth = cellWidth * 2 - 20
    cardHeight = cellHeight - 20
    cardTop = 10
    for i in range(len(app.plantCards)):
        cardLeft = app.boardLeft + cardWidth*i + 10
        right = cardLeft + cardWidth
        bottom = cardTop + cardHeight

        if (cardLeft <= mouseX <= right) and (cardTop <= mouseY <= bottom):
            return i
    return None

def enoughSun(plantIndex):
    if app.plantCardsSunValue[plantIndex] <= app.sunCount:
        return True
    return False

def centeredMessage(app, message):
    lines = message.split('\n')
    drawImage(app.messageImg, app.width / 2, app.height / 2, align = 'center')

    lineHeight = 20
    center = len(lines) * lineHeight / 2
    for i in range(len(lines)):
        drawLabel(lines[i], app.width / 2, app.height / 2 + lineHeight * i - center, font = 'cinzel', size = 16)

def getRow(y):
    return y // 100

def getCol(x):
    return x // 100