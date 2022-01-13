import pygame
from src.blocks.Block import Block


# tường gạch
class Wall(Block):
    def __init__(self, x, y, state='f'):
        super().__init__(x, y, state=state)
        self.small = pygame.transform.scale(pygame.image.load(
            'src/sprites/blocks/wall.png'), (self.display // 2, self.display // 2))

        self.setImage()
        self.updateRect()