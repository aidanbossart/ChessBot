import chess
import random
import math

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
    
    def getPieceValue(self, piece):
        return self.values.get(piece.piece_type) if piece.color == chess.WHITE else -1*self.values.get(piece.piece_type)
    
    def getBestMove(self):
        move = self.minimaxRoot(3, True)

        return move
    
    def minimaxRoot(self, depth, isMaximizing):
        best = None
        bestValue = -9000

        if(len(list(self.board.legal_moves)) == 1):
            move = list(self.board.legal_moves)[0]
            return move


        for move in self.board.legal_moves:
            self.board.push(move)
            val = max(bestValue, self.minimax(depth - 1, -9999, 9999, False))
            self.board.pop()
            if(val > bestValue):
                bestValue = val
                best = move
        
        return best

    def evaluation(self):
        eval = 0
        for i in range(0, 64):
            if(self.board.piece_at(chess.square(i - (8*math.floor(i/8)), 7 - math.floor(i/8))) != None):
                eval = eval + self.getPieceValue(self.board.piece_at(chess.square(i - (8*math.floor(i/8)), 7 - math.floor(i/8))))
        return eval


    def minimax(self, depth, alpha, beta, isMaximizing):
        if(depth == 0):
            return -self.evaluation()
        
        moves = self.board.legal_moves

        if(isMaximizing):
            best = -9999
            for move in moves:
                self.board.push(move)
                best = max(best, self.minimax(depth -1, alpha, beta, not isMaximizing))
                self.board.pop()
                alpha = max(alpha, best)
                if(beta <= alpha):
                    break
            return best
        else:
            best = 9999
            for move in moves:
                self.board.push(move)
                best = min(best, self.minimax(depth -1, alpha, beta, not isMaximizing))
                self.board.pop()
                beta = min(beta, best)
                if(beta <= alpha):
                    break
            return best