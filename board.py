import pygame

class Board:
    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

    def drawBoard(self):
        board = pygame.Surface((100 * 8, 100 * 8))
        board.fill((241,217,181))

        for x in range(1, 8, 2):
            for y in range(0, 8, 2):
                pygame.draw.rect(board, (181,136,99), (x*100, y*100, 100, 100))

        for x in range(0, 8, 2):
            for y in range(1, 8, 2):
                pygame.draw.rect(board, (181,136,99), (x*100, y*100, 100, 100))

        self.gameDisplay.blit(board, board.get_rect())








