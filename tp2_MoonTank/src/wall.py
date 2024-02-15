import pygame
import sys
sys.path.append('src')
from color import Color


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        if color == Color.GRAY:
            self.color = Color.GRAY
            self.image = pygame.image.load('./tp2_base/assets/wall.png')
        elif color == Color.RED:
            self.color = Color.RED
            self.image = pygame.image.load('./tp2_base/assets/red.png')
        elif color == Color.GREEN:
            self.color = Color.GREEN
            self.image = pygame.image.load('./tp2_base/assets/green.png')
        elif color == Color.BLUE:
            self.color = Color.BLUE
            self.image = pygame.image.load('./tp2_base/assets/blue.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def destroy(self):
        self.kill()
