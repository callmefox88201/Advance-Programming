import random
import pygame
from pygame import sprite
from src.Bonus import Bonus
from src.Field import Field
from src.blocks.Wall import Wall
from src.tanks.Enemy import Enemy
from src.tanks.Player import Player
screenSize = width, height = 800, 650


class Loop:
    def __init__(self):
        pass

    def loop(self, levelNo):
        tankSprites = pygame.sprite.Group()
        playerGroup = pygame.sprite.Group()

        playerBullets = pygame.sprite.Group()
        enemyBullets = pygame.sprite.Group()

        lifeBonus = pygame.sprite.GroupSingle()
        boomBonus = pygame.sprite.GroupSingle()
        protectBonus = pygame.sprite.GroupSingle()

        bullets = []

        enemyCount = 10
        playerLife = 3

        pygame.init()
        screen = pygame.display.set_mode(screenSize)

        panel = pygame.sprite.Sprite()
        panel.image = pygame.image.load('src/sprites/panel.png')
        panel.rect = panel.image.get_rect()
        panel.rect.x = 650
        panel.rect.y = 0

        f = Field(levelNo)
        f.panel.add(panel)
        fieldSprites = f.fieldSpriteGroup()
        decorate = f.trees

        player = Player(playerBullets, bullets)
        playerGroup.add(player)

        pygame.font.init()
        firstEnemy = Enemy(enemyBullets, bullets, 0, 0, playerGroup, '1')

        tankSprites.add(firstEnemy)
        enemies = []
        enemies.append(firstEnemy)

        ticks = 0
        enemieAlives = True
        exitgame = False

        while not exitgame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True

            for enemy in enemies:
                if not enemy.alive():
                    enemies.remove(enemy)

            if ticks >= 300:
                if len(enemies) < 4 and enemyCount > 0 and enemyCount - len(enemies) > 0:
                    newEnemy = Enemy(enemyBullets, bullets, (random.randint(
                        0, 12)) * 50 + 2, 40, playerGroup, random.randint(0, 3))
                    while pygame.sprite.spritecollideany(newEnemy, tankSprites) or pygame.sprite.spritecollideany(newEnemy, playerGroup) or pygame.sprite.spritecollideany(newEnemy, fieldSprites):
                        newEnemy = Enemy(enemyBullets, bullets, (random.randint(
                            0, 12)) * 50 + 2, 40, playerGroup, random.randint(0, 3))
                    enemies.append(newEnemy)
                    tankSprites.add(newEnemy)
                    ticks = 0
                else:
                    ticks = 300

            tankSprites.update()
            playerGroup.update()
            playerBullets.update()
            enemyBullets.update()
            screen.fill((0, 0, 0))

            tankFields = self.spriteGrouping(tankSprites, fieldSprites)
            playerFields = self.spriteGrouping(playerGroup, fieldSprites)
            for p in playerGroup:
                tmp = self.spriteGrouping(tankFields, playerGroup)
                tmp.remove(player)
                player.checkSprite(tmp)
            for enemy in enemies:
                if enemy.alive():
                    tmp = self.spriteGrouping(tankFields, playerFields)
                    tmp.remove(enemy)
                    enemy.checkSprite(tmp)

            fieldSprites.draw(screen)
            tankSprites.draw(screen)
            lifeBonus.draw(screen)
            boomBonus.draw(screen)
            protectBonus.draw(screen)
            playerBullets.draw(screen)
            enemyBullets.draw(screen)
            playerGroup.draw(screen)
            decorate.draw(screen)
            font = pygame.font.SysFont('Comic Sans MS', 24, True)
            txtEnemyCount = font.render(
                'Enemies: ' + str(enemyCount), False, (255, 255, 255))
            txtLifeCount = font.render(
                'lifes: ' + str(playerLife), False, (255, 255, 255))
            screen.blit(txtEnemyCount, (655, 250))
            screen.blit(txtLifeCount, (655, 350))

            for p in playerGroup:
                if pygame.sprite.spritecollide(p, lifeBonus, True):
                    playerLife += 1
                if pygame.sprite.spritecollide(p, boomBonus, True):
                    for enemy in enemies:
                        if enemy.isAlive:
                            enemy.kill()
                            enemyCount -= 1
                    if enemyCount <= 0:
                        enemieAlives = False
                        return 'win'
                if pygame.sprite.spritecollide(p, protectBonus, True):
                    f.walls.add(Wall(5 * 50, 12 * 50, 'br'))
                    f.walls.add(Wall(5 * 50, 12 * 50, 'tr'))
                    f.walls.add(Wall(5 * 50, 11 * 50, 'br'))
                    f.walls.add(Wall(6 * 50, 11 * 50, 'br'))
                    f.walls.add(Wall(6 * 50, 11 * 50, 'bl'))
                    f.walls.add(Wall(7 * 50, 12 * 50, 'bl'))
                    f.walls.add(Wall(7 * 50, 12 * 50, 'tl'))
                    f.walls.add(Wall(7 * 50, 11 * 50, 'bl'))

            if len(bullets) > 0:
                for bullet in bullets:
                    if not bullet.alive():
                        bullets.remove(bullet)

                for bullet in bullets:
                    if pygame.sprite.spritecollideany(bullet, f.walls) \
                        or pygame.sprite.spritecollideany(bullet, f.steels) \
                            or pygame.sprite.spritecollideany(bullet, f.ices)\
                            or pygame.sprite.spritecollideany(bullet, f.panel):
                        collided = pygame.sprite.spritecollide(
                            bullet, f.walls, True)
                        fieldSprites = f.fieldSpriteGroup()
                        bullet.kill()
                for bullet in bullets:
                    if pygame.sprite.spritecollideany(bullet, f.city):
                        pygame.sprite.spritecollide(bullet, f.city, True)
                        return 'lose'

                for bullet in bullets:
                    if pygame.sprite.spritecollideany(bullet, playerGroup):
                        collided = pygame.sprite.spritecollide(
                            bullet, playerGroup, False)
                        playerLife -= 1
                        if playerLife <= 0:
                            return 'lose'
                        else:
                            for i in collided:
                                i.respawn()
                            for tank in tankSprites:
                                tank.player = playerGroup
                        if playerLife != 3 and len(lifeBonus) == 0 and random.randint(0, 1) == 0:
                            life = Bonus(random.randint(
                                1, 11) * 50 + 2, random.randint(1, 11) * 50 + 2, 'life')
                            lifeBonus.add(life)
                        bullet.kill()

                for bullet in playerBullets:
                    if pygame.sprite.spritecollide(bullet, tankSprites, True):
                        if enemieAlives:
                            enemyCount -= 1
                        if enemyCount <= 0:
                            enemieAlives = False
                            return 'win'
                        bullet.kill()
                        if enemyCount > 0:
                            for enemy in enemies:
                                if not enemy.isAlive:
                                    newEnemy = Enemy(enemyBullets, bullets, (random.randint(
                                        0, 12)) * 50 + 2, 40, playerGroup, random.randint(0, 3))
                                    while pygame.sprite.spritecollideany(newEnemy, tankSprites) or pygame.sprite.spritecollideany(newEnemy, playerGroup) or pygame.sprite.spritecollideany(newEnemy, fieldSprites):
                                        newEnemy = Enemy(enemyBullets, bullets, (random.randint(
                                            0, 12)) * 50 + 2, 40, playerGroup, random.randint(0, 3))
                                    enemy = newEnemy
                                    tankSprites.add(enemy)
                        if random.randint(0, 10) == 0:
                            boom = Bonus(random.randint(
                                1, 11) * 50 + 2, random.randint(1, 11) * 50 + 2, 'boom')
                            boomBonus.add(boom)
                        if random.randint(0, 10) == 1:
                            protect = Bonus(random.randint(
                                1, 11) * 50 + 2, random.randint(1, 11) * 50 + 2, 'protect')
                            protectBonus.add(protect)

                pygame.sprite.groupcollide(
                    enemyBullets, playerBullets, True, True)

            pygame.display.flip()
            pygame.time.wait(10)
            ticks += 1
        return 'exit'

    def spriteGrouping(self, tanks, fields):
        spriteGroup = pygame.sprite.Group()
        for tank in tanks:
            spriteGroup.add(tank)
        for field in fields:
            spriteGroup.add(field)
        return spriteGroup
