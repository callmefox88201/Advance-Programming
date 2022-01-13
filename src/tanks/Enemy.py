import pygame
import random
from src.tanks.Tank import Tank
from src.tanks.Bullet import Bullet

width, height = 800, 650


class Enemy(Tank):
    def __init__(self, spriteGroup, bullets, x, y, player, mode):
        imageUp = pygame.transform.scale(
            pygame.image.load('src/sprites/enemy.png'), (40, 40))
        super().__init__(spriteGroup, bullets, imageUp)
        self.rect.centerx = x
        self.rect.bottom = y
        self.distance = 0
        self.checkNumber = 0
        self.bullet = Bullet(0, 0, 0)
        self.bullet.kill()
        self.player = player
        self.isGlitched = False
        self.mode = mode
        self.glitches = []
        self.delay = 250
        self.lastShot = pygame.time.get_ticks()

    def shoot(self):
        if not self.bullet.alive() and self.cooldown == 0:
            self.bullet = Bullet(
                self.rect.centerx, self.rect.top, self.direction)
            self.sprites.add(self.bullet)
            self.cooldown = 50
            self.bullets.append(self.bullet)

    def update(self):
        super().update()
        self.deltaX = 0
        self.deltaY = 0
        self.chooseNumber()

        now = pygame.time.get_ticks()
        if self.mode != 3:
            if now - self.lastShot > self.delay:
                self.lastShot = now
                self.shoot()
        self.move()
        self.checkSprite()
        self.setTankSprite()
        self.checkGlitch()

    def move(self):
        if self.canMove == False:
            self.distance = 0
        self.chooseDirection()
        if self.direction == 'w':
            self.distance -= self.speed
            self.goUp()
        elif self.direction == 's':
            self.distance -= self.speed
            self.goDown()
        elif self.direction == 'a':
            self.distance -= self.speed
            self.goLeft()
        elif self.direction == 'd':
            self.distance -= self.speed
            self.goRight()

    def chooseDirection(self):
        if self.distance <= 0 and not self.isGlitched:
            direction = ['a', 'w', 's', 'd']
            randNumber = random.randint(0, 3)
            self.direction = direction[randNumber]
            self.distance = 50 * random.randint(1, 2)
        elif self.isGlitched:
            self.isGlitched = False

    def checkGlitch(self):
        a = (self.rect.x, self.rect.y)
        self.glitches.append(a)

        if len(self.glitches) > 40:
            if self.glitches[1:] == self.glitches[:-1]:
                self.move()
                self.checkSprite()
            self.glitches = list()

    def chooseNumber(self):
        for p in self.player:
            if self.mode == 3:
                if self.checkClose(p.rect.y, self.rect.y):
                    if p.rect.x > self.rect.x:
                        self.direction = 'd'
                    else:
                        self.direction = 'a'
                    self.shoot()
                    self.isGlitched = True
                elif self.checkClose(p.rect.x, self.rect.x):
                    if p.rect.y > self.rect.y:
                        self.direction = 's'
                    else:
                        self.direction = 'w'
                    self.shoot()
                    self.isGlitched = True
            elif self.mode == 2:
                choice = random.randint(0, 5)
                if choice <= 4:
                    if self.checkClose(p.rect.y, self.rect.y):
                        if p.rect.x > self.rect.x:
                            self.direction = 'd'
                        else:
                            self.direction = 'a'
                        self.shoot()
                        self.direction_glitch = True
                    elif self.checkClose(p.rect.x, self.rect.x):
                        if p.rect.y > self.rect.y:
                            self.direction = 's'
                        else:
                            self.direction = 'w'
                        self.shoot()
                        self.isGlitched = True
            elif self.mode == 1:
                if self.checkClose(p.rect.y, self.rect.y):
                    if p.rect.x > self.rect.x and self.direction == 'd':
                        self.shoot()
                    elif p.rect.x < self.rect.x and self.direction == 'a':
                        self.shoot()
                    self.direction_glitch = True
                elif self.checkClose(p.rect.x, self.rect.x):
                    if p.rect.y > self.rect.y and self.direction == 's':
                        self.shoot()
                    elif p.rect.y < self.rect.y and self.direction == 'w':
                        self.shoot()
                    self.isGlitched = True

    def checkClose(self, a, b):
        if abs(a-b) < 6:
            return True
        return False
