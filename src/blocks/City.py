import pygame
from src.blocks.Block import Block


# thành phố (nhà chính)
class City(Block):
    def __init__(self, x, y, state='f'):
        super().__init__(x, y, state)

        self.full = pygame.transform.scale(pygame.image.load(
            'src/sprites/blocks/city.png'), (self.display, self.display))

        self.setImage()
        self.updateRect()
