import chess
import random

class ChessAI():
    def __init__(self, board):
        self.board = board
        self.values = {
            chess.PAWN: 10,
            chess.KNIGHT: 30,
            chess.BISHOP: 30,
            chess.ROOK: 50,
            chess.QUEEN: 90,
            chess.KING: 900
        }
    
    def randomMove(self):
        #print(type(self.board.legal_moves))
        #move = list(self.board.legal_moves)[random.randint(0, self.board.legal_moves.count()-1)]
        move = self.getBestMove()
        return move
    
    def getPieceValue(self, piece):
        print(self.values.get(piece.piece_type))
        return self.values.get(piece.piece_type)
    
    def getBestMove(self):
        best = None
        bestValue = -9000

        for move in self.board.legal_moves:
            if(self.board.is_capture(move) == True):
                piece = self.board.piece_at(move.to_square)
                if(self.getPieceValue(piece) > bestValue):
                    best = move
                    bestValue = self.getPieceValue(piece)
        
        if(best == None):
            best = list(self.board.legal_moves)[random.randint(0, self.board.legal_moves.count()-1)]
        
        return best