from board import Board
from pieces import *
import pygame
import time

DIMENSION = 8
MAX_FPS = 30

print("Starting")

pygame.init()

font = pygame.font.SysFont("Courier", 16)

gameDisplay = pygame.display.set_mode((800,800))

pygame.display.set_caption("Chess")

board = Board(gameDisplay)

pygame.display.update()

frameCount = 0
frameRate = 0
t0 = time.clock()

clock = pygame.time.Clock()

pieces = []
pieces.append(Pawn(gameDisplay, 1, 1, "sprites/whitePawn.png"))

while True:
    clock.tick(MAX_FPS) # Set the max FPS

    event = pygame.event.poll()
    if(event.type == pygame.QUIT):
        break
    if(event.type == pygame.KEYDOWN):
        if(event.dict["key"] == 27):
            break
    if(event.type == pygame.MOUSEBUTTONDOWN):
        pos = event.dict["pos"]
        for piece in pieces:
            if piece.containsPoint(pos):
                print(piece.x)

    frameCount += 1
    if(frameCount % 500 == 0):
        t1 = time.clock()
        frameRate = 500 / (t1-t0)
        t0 = t1
    
    board.drawBoard()

    for piece in pieces:
        piece.drawPiece()
    
    fpsView = font.render("Frame = {0},  rate = {1:.2f} fps"
                  .format(frameCount, frameRate), True, (0,0,0))

    gameDisplay.blit(fpsView, (10, 10))

    pygame.display.flip()