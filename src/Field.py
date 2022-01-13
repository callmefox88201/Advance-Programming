import pygame
from src.blocks.City import City
from src.blocks.Ice import Ice
from src.blocks.Sea import Sea
from src.blocks.Steel import Steel
from src.blocks.Tree import Tree
from src.blocks.Wall import Wall

display = 50


class Field:
    def __init__(self, levelNo):
        self.walls = pygame.sprite.Group()
        self.steels = pygame.sprite.Group()
        self.trees = pygame.sprite.Group()
        self.seas = pygame.sprite.Group()
        self.ices = pygame.sprite.Group()
        self.panel = pygame.sprite.Group()
        self.city = pygame.sprite.GroupSingle()
        self.levelPath = 'src/levels/level' + levelNo + ".txt"
        self.readMap()
        self.addBlocks()

    def readMap(self):
        with open(self.levelPath, 'r') as f:
            self.levelMap = f.read().splitlines()

    def addBlocks(self):
        x, y = 0, 0
        for s in self.levelMap:
            for c in s:
                if c != 'z':
                    if c == '8':
                        self.walls.add(Wall(x * display, y * display, 'tl'))
                        self.walls.add(Wall(x * display, y * display, 'tr'))
                    elif c == '4':
                        self.walls.add(Wall(x * display, y * display, 'tl'))
                        self.walls.add(Wall(x * display, y * display, 'bl'))
                    elif c == '6':
                        self.walls.add(Wall(x * display, y * display, 'tr'))
                        self.walls.add(Wall(x * display, y * display, 'br'))
                    elif c == '2':
                        self.walls.add(Wall(x * display, y * display, 'bl'))
                        self.walls.add(Wall(x * display, y * display, 'br'))
                    elif c == '5':
                        self.walls.add(Wall(x * display, y * display, 'tl'))
                        self.walls.add(Wall(x * display, y * display, 'tr'))
                        self.walls.add(Wall(x * display, y * display, 'bl'))
                        self.walls.add(Wall(x * display, y * display, 'br'))
                    elif c == '7':
                        self.walls.add(Wall(x * display, y * display, 'tl'))
                    elif c == '9':
                        self.walls.add(Wall(x * display, y * display, 'tr'))
                    elif c == '1':
                        self.walls.add(Wall(x * display, y * display, 'bl'))
                    elif c == '3':
                        self.walls.add(Wall(x * display, y * display, 'br'))
                    elif c == 'w':
                        self.steels.add(Steel(x * display, y * display, 'tl'))
                        self.steels.add(Steel(x * display, y * display, 'tr'))
                    elif c == 'a':
                        self.steels.add(Steel(x * display, y * display, 'tl'))
                        self.steels.add(Steel(x * display, y * display, 'bl'))
                    elif c == 's':
                        self.steels.add(Steel(x * display, y * display, 'bl'))
                        self.steels.add(Steel(x * display, y * display, 'br'))
                    elif c == 'd':
                        self.steels.add(Steel(x * display, y * display, 'tr'))
                        self.steels.add(Steel(x * display, y * display, 'br'))
                    elif c == 'q':
                        self.steels.add(Steel(x * display, y * display, 'tl'))
                        self.steels.add(Steel(x * display, y * display, 'tr'))
                        self.steels.add(Steel(x * display, y * display, 'bl'))
                        self.steels.add(Steel(x * display, y * display, 'br'))
                    elif c == 'M':
                        self.walls.add(Wall(x * display, y * display, 'tl'))
                        self.walls.add(Wall(x * display, y * display, 'tr'))
                        self.steels.add(Steel(x * display, y * display, 'bl'))
                        self.steels.add(Steel(x * display, y * display, 'br'))
                    elif c == 'i':
                        self.ices.add(Ice(x * display, y * display))
                    elif c == 't':
                        self.trees.add(Tree(x * display, y * display))
                    elif c == 'r':
                        self.seas.add(Sea(x * display, y * display))
                    elif c == 'c':
                        self.city.add(City(x * display, y * display))
                x += 1
            x = 0
            y += 1

    def fieldSpriteGroup(self):
        fieldSprite = pygame.sprite.Group()
        for block in self.walls:
            fieldSprite.add(block)
        for block in self.ices:
            fieldSprite.add(block)
        for block in self.seas:
            fieldSprite.add(block)
        for block in self.steels:
            fieldSprite.add(block)
        for block in self.city:
            fieldSprite.add(block)
        fieldSprite.add(self.panel)
        return fieldSprite
