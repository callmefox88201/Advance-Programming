import pygame
from src.blocks.Block import Block


# thép
class Steel(Block):
    def __init__(self, x, y, state='f'):
        super().__init__(x, y, state)

        self.small = pygame.transform.scale(pygame.image.load(
            'src/sprites/blocks/steel.png'), (self.display // 2, self.display // 2))

        self.setImage()
        self.updateRect()
