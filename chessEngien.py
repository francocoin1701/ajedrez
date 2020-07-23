"""
this class is responsible of store all the information about the current state of our game. it will also be
responsible for determining the values moves at the current state. it will also keep a move log
"""


class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "bR"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "wR"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.moveFunctions = {"p": self.getPawnMoves, "R": self.getRookMoves, "N": self.getKnigtMoves, 
                              "B": self.getBishopMoves, "Q": self.getQuinMoves, "K": self.getKingMoves}
        self.whiteToMove = True
        self.moveLog = []
    def makeMove(self, Move):
        self.board[Move.startRow][Move.startCol] = "--"
        self.board[Move.endRow][Move.endCol] = Move.pieceMoved
        self.moveLog.append(Move)
        self.whiteToMove = not self.whiteToMove

    # undo the last move made
    def undoMove(self):
        if len(self.moveLog) != 0:
            Move = self.moveLog.pop()
            self.board[Move.startRow][Move.startCol] = Move.pieceMoved
            self.board[Move.endRow][Move.endCol] = Move.pieceCapture
            self.whiteToMove = not self.whiteToMove 
    
    # all moves considering checks
    def getValidMoves(self):
        return self.getAllPosibleMoves() # por a hora est   a funcion retorna esto

    # all moves whitout considering checks

    def getAllPosibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                
                
                if ((turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove)):
                    piece = self.board[r][c][1]
                    print(turn)
                    #print(piece)
                    self.moveFunctions[piece](r,c,moves)                       
        return moves
    def getPawnMoves(self,r,c,moves):
        if self.whiteToMove:
            if self.board[r-1][c] == "--":
                moves.append(Move((r,c),(r-1,c),self.board))
                if r == 6 and self.board[r-2][c] == "--":
                    moves.append(Move((r,c),(r-2,c), self.board))
            if c - 1 >= 0:
                if self.board[r-1][c-1][0] == "b":
                    moves.append(Move((r,c),(r-1,c-1),self.board))
            if c + 1 <= 7:
                if self.board[r-1][c+1][0] == "b":
                    moves.append(Move((r,c),(r-1,c+1),self.board))
            
                    
        else:    
            if self.board[r+1][c] == "--": # 1 square move
                moves.append(Move((r,c),(r+1,c),self.board))
            
                if r == 1 and self.board[r+2][c] == "--":
                    moves.append(Move((r,c),(r+2,c),self.board))

            if c - 1 >= 0:
                if self.board[r+1][c-1][0] == "w":
                    moves.append(Move((r,c),(r+1,c-1),self.board))
            if c + 1 <= 7:
                if self.board[r+1][c+1][0] == "w":
                    moves.append(Move((r,c),(r+1,c+1),self.board))     
            
         
               
    def getRookMoves(self,r,c,moves):
        directions = ((-1,0),(0,-1),(1,0),(0,1))
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1,8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(Move((r,c),(endRow,endCol),self.board))

                    elif endPiece[0] == enemyColor:
                        moves.append(Move((r,c),(endRow,endCol),self.board))
                        break
                    else:
                        break
                else:
                    break     
    def getKnigtMoves(self,r,c,moves):
        pass
    
    def getBishopMoves(self,r,c,moves):
        pass
    
    def getQuinMoves(self,r,c,moves):
        pass

    def getKingMoves(self,r,c,moves):
        pass                  

class Move():
    filesToRows = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    rowsToFiles = {v:k for k,v in filesToRows.items()}
    ranksToCols = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    colsToRank = {v:k for k,v in ranksToCols.items()}

    def __init__(self, sqStart, sqEnd, board):
        self.startRow = sqStart[0]
        self.startCol = sqStart[1]
        self.endRow = sqEnd[0]
        self.endCol = sqEnd[1]
        self.pieceMoved = board[self.startRow][self.startCol] 
        self.pieceCapture = board[self.endRow][self.endCol] 
        self.siteId = self.startRow*1000+self.startCol*100+self.endRow*10+self.endCol
        print(self.siteId) 

    def __eq__(self,other):
        if isinstance(other, Move):
            return self.siteId == other.siteId
        return False    
        

    def getChessNotation(self):
        return self.getRanckFiles(self.startRow,self.startCol)+self.getRanckFiles(self.endRow,self.endCol)

    def getRanckFiles(self,r,c):
        return self.colsToRank[c]+self.rowsToFiles[r]    