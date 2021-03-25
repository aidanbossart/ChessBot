import pygame
import ChessEngine

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
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if(piece != "--"):
                screen.blit(IMAGES[piece], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    gs = ChessEngine.GameState()
    loadImages()
    running = True

    sqSelected = ()
    playerClicks = []

    while running:
        for ev in pygame.event.get():
            if(ev.type == pygame.QUIT):
                running = False
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
                    if(len(playerClicks) == 2):
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
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