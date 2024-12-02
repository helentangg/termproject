from cmu_graphics import *
from PIL import Image
import os

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
    app.sunCount = 0
    app.plantCards = ['peashooter', 'peashooter', 'peashooter', 'peashooter']

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
        plantImg = Image.open(os.path.join('src/images', f'{app.plantCards[i]}.png'))
        plantImg = plantImg.resize((60, 60))
        plantImg = CMUImage(plantImg)
        drawImage(plantImg, app.boardLeft + cardWidth*i + 10 + 90 + i*20, 50, align = 'center')

def drawCard(app, x, y):
    cellWidth, cellHeight = getCellSize(app)
    cardWidth = cellWidth * 2 - 20
    cardHeight = cellHeight - 20
    drawRect(x, y, cardWidth, cardHeight, fill = 'white', opacity = 50, border = 'black')
    drawRect(x, y, cardWidth, cardHeight, fill = None, border = 'black')

def drawSunbar(app):
    drawRect(app.menuWidth + app.boardLeft, 0, app.sunbarWidth, app.sunbarHeight, fill = 'grey', opacity = 10)

    cellWidth, cellHeight = getCellSize(app)
    drawImage(app.sunImg, app.menuWidth + app.boardLeft + cellWidth + 10, 10)
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
            return True
    return False