from cmu_graphics import *

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