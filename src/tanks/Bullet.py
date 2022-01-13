import pygame

width, height = 800, 650


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.direction = direction
        self.image = pygame.transform.scale(
            pygame.image.load('src/sprites/bullet.png'), (10, 20))
        self.rect = self.image.get_rect()
        if direction == 'w':
            self.rect.x = x - 5
            self.rect.y = y - 20
            self.deltaY = -self.speed
        elif direction == 'a':
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect.x = x - 30
            self.rect.y = y + 15
            self.deltaX = -self.speed
        elif direction == 'd':
            self.image = pygame.transform.rotate(self.image, 270)
            self.rect.x = x + 30
            self.rect.y = y + 15
            self.deltaX = self.speed
        elif direction == 's':
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect.x = x - 5
            self.rect.y = y + 40
            self.deltaY = self.speed

    def update(self):
        if self.direction == 'w':
            self.rect.y += self.deltaY
        if self.direction == 'd':
            self.rect.x += self.deltaX
        if self.direction == 's':
            self.rect.y += self.deltaY
        if self.direction == 'a':
            self.rect.x += self.deltaX
        if self.rect.top < 0 or self.rect.bottom > height or self.rect.right > width or self.rect.left < 0:
            self.kill()
