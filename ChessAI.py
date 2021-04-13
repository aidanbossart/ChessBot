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
    
    def randomMove(self):
        #print(type(self.board.legal_moves))
        #move = list(self.board.legal_moves)[random.randint(0, self.board.legal_moves.count()-1)]
        move = self.getBestMove()
        return move
    
    def getPieceValue(self, piece):
        #if(piece.color == chess.WHITE):
        #    self.values.get(piece.piece_type)
        #elif(piece.color == chess.BLACK):
        #    self.values.get(piece.piece_type)
        return self.values.get(piece.piece_type) if piece.color == chess.WHITE else -1*self.values.get(piece.piece_type)
    
    def getBestMove(self):
        print("getting best move")
        move = self.minimaxRoot(3, True)
        #move = self.minimax(3, -9999, 9999, True)
        print(move)

        return move
    
    def minimaxRoot(self, depth, isMaximizing):
        best = None
        bestValue = -9000

        for move in self.board.legal_moves:
            self.board.push(move)
            val = max(bestValue, self.minimax(depth - 1, -9999, 9999, False))
            print(val)
            self.board.pop()
            if(val > bestValue):
                bestValue = val
                best = move
        
        return best

    def evaluation(self):
        eval = 0
        for i in range(0, 64):
            #print(self.board.piece_at(chess.square(i - (8*math.floor(i/8)), 7 - math.floor(i/8))))
            if(self.board.piece_at(chess.square(i - (8*math.floor(i/8)), 7 - math.floor(i/8))) != None):
                eval = eval + self.getPieceValue(self.board.piece_at(chess.square(i - (8*math.floor(i/8)), 7 - math.floor(i/8))))
        return eval


    def minimax(self, depth, alpha, beta, isMaximizing):
        if(depth == 0):
            #print("EVAL = "+ str(-self.evaluation()))
            return -self.evaluation()
        
        moves = self.board.legal_moves

        if(isMaximizing):
            best = -9999
            for move in moves:
                self.board.push(move)
                best = max(best, self.minimax(depth -1, alpha, beta, not isMaximizing))
                print("BEST = "+str(best))
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