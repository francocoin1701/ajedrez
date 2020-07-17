"""
this class is responsible of store all the information about the current state of our game. it will also be
responsible for determining the values moves at the current state. it will also keep a move log
"""


class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

class move():
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    rowsToRank = {k:v for v,k in ranksToRows.items()}
    filesToCols = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    colsToFiles = {k:v for v,k in filesToCols.items()}

    def __init__(self, sqStart, sqEnd, board):
        self.startRow = sqStart[1]
        self.startCol = sqStart[0]
        self.endRow = sqEnd[1]
        self.endCol = sqEnd[0]
        self.pieceMoved = board[self.startRow][self.startCol] 
        self.pieceCapture = board[self.endRow][self.endCol]           

    def getChessNotation(self):
        return self.getRanckFiles(self.startCol,self.startRow)+self.getRanckFiles(self.endCol,self.endRow)

    def getRanckFiles(self,r,c):
        return self.colsToFiles[c]+self.rowsToRank[r]    