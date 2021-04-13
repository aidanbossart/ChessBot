import chess

class GameState():
    def __init__(self):
        self.board = chess.Board()
    
    def makeMove(self, code):
        self.board.push(code)