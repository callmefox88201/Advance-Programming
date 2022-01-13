import pygame
from src.blocks.Block import Block


# cây
class Tree(Block):
    def __init__(self, x, y, state='f'):
        super().__init__(x, y, state)
        # lần lượt là các hình ảnh khối to và nhỏ (bằng 1/4)
        self.full = pygame.transform.scale(pygame.image.load(
            'src/sprites/blocks/tree.png'), (self.display, self.display))
        self.small = pygame.transform.scale(pygame.image.load(
            'src/sprites/blocks/tree.png'), (self.display // 2, self.display // 2))

        self.setImage()
        self.updateRect()
