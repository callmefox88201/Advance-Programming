import pygame


class Bonus(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("src/sprites/bonuses/"+name+".png"), (44, 44))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
