import pygame
from wall import *
from collectible import *
from level import *
from enum import Enum

class State(Enum):
    MENU = 1
    PLAY = 2
    GAME_OVER = 3

class Game():
    def __init__(self):
        super().__init__()
        self.walls = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.level = 0
        self.state = State.MENU

    def update(self):
        for projectile in self.projectiles:
            projectile.update()

    def loadLevel(self, player):

        self.walls.empty()
        self.projectiles.empty()
        self.collectibles.empty()

        level = levels[self.level]
        level_map = level["map"]
        bullet_counts = level["bullets"]

        y=0
        for line in level_map:
            x=0
            for char in line:
                if char == "o":
                    wall = Wall(x, y, Color.GRAY)
                    self.walls.add(wall)
                elif char == " ":
                    pass
                elif char == "r":
                    wall = Wall(x, y, Color.RED)
                    self.walls.add(wall)
                elif char == "g":
                    wall = Wall(x, y, Color.GREEN)
                    self.walls.add(wall)
                elif char == "b":
                    wall = Wall(x, y, Color.BLUE)
                    self.walls.add(wall)
                elif char == "z":
                    bullet = Bullet(x, y, Color.RED)
                    self.collectibles.add(bullet)
                elif char == "x":
                    bullet = Bullet(x, y, Color.GREEN)
                    self.collectibles.add(bullet)
                elif char == "c":
                    bullet = Bullet(x, y, Color.BLUE)
                    self.collectibles.add(bullet)
                elif char == "s":
                    player.rect.x = x
                    player.rect.y = y
                    player.orientation = Orientation.RIGHT
                elif char == "e":
                    flag = Flag(x, y)
                    self.collectibles.add(flag)
                x+=100
            y+= 100
        
        player.bulletR = bullet_counts[0]
        player.bulletG = bullet_counts[1]
        player.bulletB = bullet_counts[2]