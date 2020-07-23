"""
this is our main drive file. it will be responsible for handling user input and display the currentState objects
"""

import pygame as p
import chessEngien

WIDTH = HEIGHT = 512  # otra opcion podria ser 400
DIMENCIONS = 8  # dimencions of chess board are of 8 x 8
SQ_SIZE = HEIGHT // DIMENCIONS
MAX_FPS = 15
IMAGES = {}


# initialize a global dictionary of image. This be called exactly once in the main function
def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "bp", "bR", "bN", "bB", "bQ", "bK", "bB", "bN",
              "bR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("img/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        # NOTE: we can access an image by saying IMAGES["wp"]


# the main driver for our code. this will handler the user input and update the graphics
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngien.GameState()
    validMoves = gs.getValidMoves()
    madeMove = False
    loadImages()
    sqSelec = ()
    playerClicks = []
    running = True
    while running:

        for e in p.event.get():
            #print(e)
            if e.type == p.QUIT:
                running = False

            elif e.type == p.MOUSEBUTTONDOWN:
                locations = p.mouse.get_pos()
                col = locations[0]//SQ_SIZE
                row = locations[1]//SQ_SIZE
                if sqSelec == (row, col):
                    sqSelec = ()
                    playerClicks = []

                else:
                    sqSelec = (row, col)
                    playerClicks.append(sqSelec)    

                if len(playerClicks) == 2:
                    move = chessEngien.Move(playerClicks[0],playerClicks[1],gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        madeMove = True                      
                    
                    sqSelec = ()
                    playerClicks = []

            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    madeMove = True
        if madeMove:
            validMoves = gs.getValidMoves()
            madeMove = False
        
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        
        p.display.flip()


# draw the squares on the board.
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPices(screen, gs.board)


# draw the squares on board. the top left square is always light

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENCIONS):
        for c in range(DIMENCIONS):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPices(screen, board):
    for r in range(DIMENCIONS):
        for c in range(DIMENCIONS):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()