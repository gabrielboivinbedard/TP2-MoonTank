import pygame
from abc import ABC, abstractmethod 
import sys
from main import sounds_path
import os

sys.path.append('src')
from color import Color
from player import *

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
            self.image = pygame.image.load('./tp2_base/assets/bulletR.png')
        elif color == Color.GREEN:
            self.color = Color.GREEN
            self.image = pygame.image.load('./tp2_base/assets/bulletG.png')
        elif color == Color.BLUE:
            self.color = Color.BLUE
            self.image = pygame.image.load('./tp2_base/assets/bulletB.png')
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
        self.image = pygame.image.load('./tp2_base/assets/flag.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def collect(self, player):
        
        self.kill()
