import pygame
import chess
import chess.svg
import ChessAI
import io
import math

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
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

def drawDrag(screen, board, square):
    symbol = board.piece_at(square)
    if(symbol == None):
        return
    symbol = symbol.symbol()

    if(symbol.islower()):
        symbol = symbol.upper()
        if(symbol == 'P'):
            symbol = 'p'
        screen.blit(IMAGES[str("b" + symbol)], pygame.Rect(pygame.mouse.get_pos()[0]-SQ_SIZE/2, pygame.mouse.get_pos()[1]-SQ_SIZE/2, SQ_SIZE, SQ_SIZE))
        
    elif(symbol.isupper()):
        if(symbol == 'P'):
            symbol = 'p'
        screen.blit(IMAGES[str("w" + symbol)], pygame.Rect(pygame.mouse.get_pos()[0]-SQ_SIZE/2, pygame.mouse.get_pos()[1]-SQ_SIZE/2, SQ_SIZE, SQ_SIZE))

def drawGameState(screen, board):
    drawBoard(screen)
    drawPieces(screen, board)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    board = chess.Board()

    ai = ChessAI.ChessAI(board)

    drag = False

    loadImages()
    running = True

    mouse_pos = ()

    sqSelected = ()
    playerClicks = []

    while running:
        if(board.is_checkmate() == True):
            print("CHECKMATE")
            exit()
        if(board.is_stalemate() == True):
            print("STALEMATE")
            exit()

        if(board.turn == chess.BLACK):
            board.push(ai.getBestMove())

        for ev in pygame.event.get():
            if(ev.type == pygame.QUIT):
                running = False
            elif(ev.type == pygame.MOUSEBUTTONDOWN):
                drag = True
                loc = pygame.mouse.get_pos()
                col = loc[0]//SQ_SIZE
                row = loc[1]//SQ_SIZE

                sqSelected = chess.square(col, 7-row)

            elif(ev.type == pygame.MOUSEMOTION):
                if(drag == True):
                    mouse_pos = pygame.mouse.get_pos()
                    
            elif(ev.type == pygame.MOUSEBUTTONUP):
                drag = False
                mouse_pos = pygame.mouse.get_pos()

                col = mouse_pos[0]//SQ_SIZE
                row = mouse_pos[1]//SQ_SIZE

                move = chess.Move(chess.square(file_index=chess.square_file(sqSelected), rank_index=chess.square_rank(sqSelected)), chess.square(file_index=col, rank_index=7-row))

                if(move in board.legal_moves):
                    board.push(move)

                sqSelected = ()
                
            elif(ev.type == pygame.KEYDOWN):
                if(ev.key == pygame.K_z):
                    gs.undoMove()
        
        clock.tick(MAX_FPS)

        drawGameState(screen, board)
        if(drag == True):
            drawDrag(screen, board, sqSelected)

        pygame.display.flip()

if __name__ == "__main__":
    main()