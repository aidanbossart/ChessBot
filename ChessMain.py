import pygame
import chess
import chess.svg
import ChessEngine
import ChessAI
import io
import math
#from svglib.svglib import svg2rlg

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("sprites/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def drawBoard(screen):
    colors = [(235, 235, 208), (119, 148, 85)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    piece_map = board.piece_map()
    for i in range(0, 64):
        if(piece_map.get(i) != None):
            r = 7 - math.floor(i/8)
            c = i - (8*math.floor(i/8))

            symbol = piece_map[i].symbol()

            if(symbol.islower()):
                symbol = symbol.upper()
                if(symbol == 'P'):
                    symbol = 'p'
                screen.blit(IMAGES[str("b" + symbol)], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                
            elif(symbol.isupper()):
                if(symbol == 'P'):
                    symbol = 'p'
                screen.blit(IMAGES[str("w" + symbol)], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    gs = ChessEngine.GameState()

    ai = ChessAI.ChessAI(gs.board)

    validMoves = gs.getValidMoves()
    modeMade = False


    loadImages()
    running = True

    sqSelected = ()
    playerClicks = []

    while running:
        for ev in pygame.event.get():
            if(ev.type == pygame.QUIT):
                running = False
            elif(gs.board.turn == chess.BLACK):
                        gs.makeMove(ai.randomMove())
            elif(ev.type == pygame.MOUSEBUTTONDOWN):
                loc = pygame.mouse.get_pos()
                col = loc[0]//SQ_SIZE
                row = loc[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                    if(len(playerClicks) == 2 and gs.board.turn == chess.WHITE):

                        move = chess.Move(chess.square(file_index=playerClicks[0][1], rank_index=7-playerClicks[0][0]), chess.square(file_index=playerClicks[1][1], rank_index=7-playerClicks[1][0]))
                        if(move in gs.board.legal_moves):
                            gs.makeMove(move)

                        
                        sqSelected = ()
                        playerClicks = []
            elif(ev.type == pygame.KEYDOWN):
                if(ev.key == pygame.K_z):
                    gs.undoMove()

        
        clock.tick(MAX_FPS)

        drawGameState(screen, gs)

        pygame.display.flip()

if __name__ == "__main__":
    main()