import pygame
from abc import ABC, abstractmethod 
import sys
sys.path.append('src')
from color import Color
from orientation import *


colorRed = [255, 0, 0]

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, orientation):
        super().__init__()
        

        if color == Color.RED:
            self.color = Color.RED
            self.image = pygame.image.load('./tp2_base/assets/br.png')
        elif color == Color.GREEN:
            self.color = Color.GREEN
            self.image = pygame.image.load('./tp2_base/assets/bg.png')
        elif color == Color.BLUE:
            self.color = Color.BLUE
            self.image = pygame.image.load('./tp2_base/assets/bb.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 12
        self.orientation = orientation
    
    def update(self):

        if self.orientation == Orientation.LEFT:
            self.rect.x -= self.speed
        elif self.orientation == Orientation.RIGHT:
            self.rect.x += self.speed
        elif self.orientation == Orientation.UP:
            self.rect.y -= self.speed
        elif self.orientation == Orientation.DOWN:
            self.rect.y += self.speed

    def destroy(self):
        self.kill()