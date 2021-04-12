import chess
import random

class ChessAI():
    def __init__(self, board):
        self.board = board
    
    def randomMove(self):
        #print(type(self.board.legal_moves))
        move = list(self.board.legal_moves)[random.randint(0, self.board.legal_moves.count()-1)]
        return move