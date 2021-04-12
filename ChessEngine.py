import chess

class GameState():
    def __init__(self):

        self.board = chess.Board()

        self.whiteToMove = True
        self.moveLog = []
        print(self.board)
    
    def makeMove(self, code):
        self.board.push(code)
    
    def undoMove(self):
        if(len(self.moveLog) != 0):
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove