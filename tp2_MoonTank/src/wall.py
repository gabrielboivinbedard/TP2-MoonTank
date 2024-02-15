import pygame
from src.color import Color
from src.path import *
import os

wall_path = os.path.join(asset_path, 'wall.png')
red_wall_path = os.path.join(asset_path, 'red.png')
green_wall_path = os.path.join(asset_path, 'green.png')
blue_wall_path = os.path.join(asset_path, 'blue.png')

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        if color == Color.GRAY:
            self.color = Color.GRAY
            self.image = pygame.image.load(wall_path)
        elif color == Color.RED:
            self.color = Color.RED
            self.image = pygame.image.load(red_wall_path)
        elif color == Color.GREEN:
            self.color = Color.GREEN
            self.image = pygame.image.load(green_wall_path)
        elif color == Color.BLUE:
            self.color = Color.BLUE
            self.image = pygame.image.load(blue_wall_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def destroy(self):
        self.kill()
