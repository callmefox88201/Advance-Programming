import pygame


# các khối trong game: gạch, biển, cây, ...
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, state='f'):
        # hiển thị trên 50px (ngang, dọc)
        self.display = 50

        # lần lượt là các hình ảnh khối to và nhỏ (bằng 1/4)
        self.full = pygame.transform.scale(pygame.image.load(
            'src/sprites/blocks/block.png'), (self.display, self.display))
        self.small = pygame.transform.scale(pygame.image.load(
            'src/sprites/blocks/block.png'), (self.display // 2, self.display // 2))

        pygame.sprite.Sprite.__init__(self)

        # biến trạng thái
        self.state = state

        # biến vị trí ban đầu
        self.startX = x
        self.startY = y

        # biến vị trí hiện tại
        self.currentX = x
        self.currentY = y

        self.stateNo = 1
        self.setImage()
        self.updateRect()

    # update lại rect của khối
    def updateRect(self):
        if self.state == 'tr':
            self.currentX = self.startX + self.display // 2
        elif self.state == 'bl':
            self.currentY = self.startY + self.display // 2
        elif self.state == 'br':
            self.currentY = self.startY + self.display // 2
            self.currentX = self.startX + self.display // 2

        self.rect = self.image.get_rect()
        self.rect.x = self.currentX
        self.rect.y = self.currentY

    # update hình ảnh
    def setImage(self):
        if self.state == 'f':
            self.image = self.full
        else:
            self.image = self.small
