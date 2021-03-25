from abc import ABC, abstractmethod
import pygame

class Piece(ABC):
    def __init__(self, gameDisplay, x, y, sprite):
        self.gameDisplay = gameDisplay
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(pygame.image.load(sprite), (100, 100))
        super().__init__()
    
    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def drawPiece(self):
        pass

    def containsPoint(self, point):
        (x, y) = point
        return (x >= self.x and x < self.x + 100 and
                y >= self.y and y < self.y + 100)

class Pawn(Piece):
    def __init__(self, gameDisplay, x, y, sprite):
        super().__init__(gameDisplay, x, y, sprite)

    def move(self, x, y):
        if(self.x == x and self.y == y-1):
            self.y += 1
    
    def drawPiece(self):
        self.gameDisplay.blit(self.sprite, (self.x, self.y))
    
    def containsPoint(self, point):
        pass