import pygame

width, height = 800, 650


class Tank(pygame.sprite.Sprite):
    def __init__(self, spriteGroup, bullets, imageUp):
        pygame.sprite.Sprite.__init__(self)
        self.imageUp = imageUp
        self.imageLeft = pygame.transform.rotate(self.imageUp, 90)
        self.imageRight = pygame.transform.rotate(self.imageUp, 270)
        self.imageDown = pygame.transform.rotate(self.imageUp, 180)

        self.isAlive = True
        self.speed = 2
        self.direction = 'w'
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2 - 155
        self.rect.bottom = height - 10
        self.deltaX = 0
        self.deltaY = 0
        self.bullets = bullets
        self.sprites = spriteGroup
        self.oldXY = self.rect.x, self.rect.y
        self.canMove = True
        self.cooldown = 0

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def goUp(self):
        self.deltaY = -self.speed
        self.direction = 'w'

    def goDown(self):
        self.deltaY = self.speed
        self.direction = 's'

    def goRight(self):
        self.deltaX = self.speed
        self.direction = 'd'

    def goLeft(self):
        self.deltaX = -self.speed
        self.direction = 'a'

    def checkSprite(self, fieldSprite=None):
        if fieldSprite != None:
            if pygame.sprite.spritecollideany(self, fieldSprite):
                self.canMove = False
                self.rect.x, self.rect.y = self.oldXY
        else:
            if self.canMove:
                self.oldXY = self.rect.x, self.rect.y
                self.rect.x += self.deltaX
                self.rect.y += self.deltaY
            else:
                self.canMove = True
                self.rect.x, self.rect.y = self.oldXY

            if self.rect.right > width:
                self.rect.right = width
                self.canMove = False
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > height:
                self.rect.bottom = height
                self.canMove = False
            if self.rect.top < 0:
                self.rect.top = 0

    def setTankSprite(self):
        if self.direction == 'w':
            self.image = self.imageUp
        elif self.direction == 's':
            self.image = self.imageDown
        elif self.direction == 'a':
            self.image = self.imageLeft
        else:
            self.image = self.imageRight
