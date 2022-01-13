import pygame
from src.blocks.Block import Block


# biển
class Sea(Block):
    def __init__(self, x, y, state='f'):
        super().__init__(x, y, state)

        self.full = pygame.transform.scale(pygame.image.load(
            'src/sprites/blocks/sea.png'), (self.display, self.display))
        self.small = pygame.transform.scale(pygame.image.load(
            'src/sprites/blocks/sea.png'), (self.display // 2, self.display // 2))

        self.setImage()
        self.updateRect()
