import pygame
from abc import ABC, abstractmethod 
import sys
from src.color import Color
from src.orientation import *
from src.path import *

print(asset_path)
br_path = os.path.join(asset_path, 'br.png')
bg_path = os.path.join(asset_path, 'bg.png')
bb_path = os.path.join(asset_path, 'bb.png')


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, orientation):
        super().__init__()
        
        if color == Color.RED:
            self.color = Color.RED
            self.image = pygame.image.load(br_path)
        elif color == Color.GREEN:
            self.color = Color.GREEN
            self.image = pygame.image.load(bg_path)
        elif color == Color.BLUE:
            self.color = Color.BLUE
            self.image = pygame.image.load(bb_path)

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