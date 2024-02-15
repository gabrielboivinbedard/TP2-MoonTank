import pygame
from orientation import *
from projectile import Projectile
from color import Color
from main import sounds_path
import os

pygame.mixer.init()

shoot_path = os.path.join(sounds_path, 'shoot.wav')
shoot = pygame.mixer.Sound(shoot_path)

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.orientation = Orientation.RIGHT
        self.original_image = pygame.image.load('./tp2_base/assets/tank.png')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.game = game
        self.speed = 6
        self.bulletR = 0
        self.bulletG = 0
        self.bulletB = 0
        self.cooldown = 400
        self.lastShot = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.orientation = Orientation.LEFT
            self.image = pygame.transform.rotate(self.original_image, 180)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.orientation = Orientation.RIGHT
            self.image = pygame.transform.rotate(self.original_image, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.orientation = Orientation.UP
            self.image = pygame.transform.rotate(self.original_image, 90)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            self.orientation = Orientation.DOWN
            self.image = pygame.transform.rotate(self.original_image, -90)

        if keys[pygame.K_z]:
            self.shoot(Color.RED)
        if keys[pygame.K_x]:
            self.shoot(Color.GREEN)
        if keys[pygame.K_c]:
            self.shoot(Color.BLUE)

    def shoot(self, color):

        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.cooldown:
            if color == Color.RED:
                if self.bulletR > 0:
                    self.bulletR -= 1
                    proj = Projectile(self.rect.center[0], self.rect.center[1], color, self.orientation)
                    self.game.projectiles.add(proj)
                    pygame.mixer.Sound.play(shoot)

            elif color == Color.GREEN:
                if self.bulletG > 0:
                    self.bulletG -= 1
                    proj = Projectile(self.rect.center[0], self.rect.center[1], color, self.orientation)
                    self.game.projectiles.add(proj)
                    pygame.mixer.Sound.play(shoot)
            elif color == Color.BLUE:
                if self.bulletB > 0:
                    self.bulletB -= 1
                    proj = Projectile(self.rect.center[0], self.rect.center[1], color, self.orientation)
                    self.game.projectiles.add(proj)
                    pygame.mixer.Sound.play(shoot)

            self.lastShot = currentTime

