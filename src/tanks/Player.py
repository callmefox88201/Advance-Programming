import pygame
from src.tanks.Tank import Tank
from src.tanks.Bullet import Bullet

class Player(Tank):
    def __init__(self, spriteGroup, bullets):
        imageUp = pygame.transform.scale(pygame.image.load('src/sprites/player.png'), (40, 40))
        super().__init__(spriteGroup, bullets, imageUp)
        self.bullet = Bullet(0, 0, 0)
        self.bullet.kill()

    def shoot(self):
        if (not self.bullet.alive() and self.cooldown <= 30) or self.cooldown == 0:
            self.bullet = Bullet(self.rect.centerx, self.rect.top, self.direction)
            self.sprites.add(self.bullet)
            self.cooldown = 45
            self.bullets.append(self.bullet)

    def update(self):
        super().update()
        self.deltaX = 0
        self.deltaY = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.goLeft()
        elif key[pygame.K_d]:
            self.goRight()
        elif key[pygame.K_w]:
            self.goUp()
        elif key[pygame.K_s]:
            self.goDown()
        if key[pygame.K_j]:
            self.shoot()
        self.checkSprite()
        self.setTankSprite()

    def respawn(self):
        self.__init__(self.sprites, self.bullets)