import pygame
from src.Loop import Loop


game = Loop()
levelNo = 1
while True:
    result = game.loop(str(levelNo))

    if result == 'win':
        levelNo += 1
    
    if result == 'exit' or result == 'lose':
        pygame.quit()
        break

    if levelNo == 4:
        levelNo = 1