import pygame
from abc import ABC, abstractmethod 
import os
from src.color import Color
from src.player import *
from src.path import *

bulletR_path = os.path.join(asset_path, 'bulletR.png')
bulletG_path = os.path.join(asset_path, 'bulletG.png')
bulletB_path = os.path.join(asset_path, 'bulletB.png')
flag_path = os.path.join(asset_path, 'flag.png')

class Collectible(ABC, pygame.sprite.Sprite): 
    @abstractmethod
    def collect(self, player): 
        pass

class Bullet(Collectible):
    def __init__(self, x, y, color):
        super().__init__()
        self.name = "bullet"
        if color == Color.RED:
            self.color = Color.RED
            self.image = pygame.image.load(bulletR_path)
        elif color == Color.GREEN:
            self.color = Color.GREEN
            self.image = pygame.image.load(bulletG_path)
        elif color == Color.BLUE:
            self.color = Color.BLUE
            self.image = pygame.image.load(bulletB_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def collect(self, player):
        if self.color == Color.RED:
            player.bulletR += 1
        elif self.color == Color.GREEN:
            player.bulletG += 1
        elif self.color == Color.BLUE:
            player.bulletB += 1
        
        self.kill()

class Flag(Collectible):
    def __init__(self, x, y):
        super().__init__()
        self.name = "flag"
        self.image = pygame.image.load(flag_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def collect(self, player):
        
        self.kill()
