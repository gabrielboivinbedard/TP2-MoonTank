import pygame
import sys
import os

project_dir = os.path.abspath(os.path.dirname(__file__))

# Append 'src' to the project directory to get the absolute path to the 'src' directory
src_path = os.path.join(project_dir, 'src')
asset_path = os.path.join(project_dir, 'assets')
sounds_path = os.path.join(project_dir, 'sounds')
# Add the absolute path to sys.path
sys.path.append(src_path)
sys.path.append(asset_path)
sys.path.append(sounds_path)

from src.player import *
from src.wall import *
from src.level import levels
from src.color import Color
from src.collectible import *
from src.orientation import *
from src.game import *

pygame.init()

win_path = os.path.join(sounds_path, 'win.wav')
win = pygame.mixer.Sound(win_path)

BG_COLOR = (153, 178, 178)

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

game = Game()

player = Player(game)

game.loadLevel(player)


selected = 1
# Main game loop
playing = True
while playing:
    keys = pygame.key.get_pressed()

    if game.state == State.MENU:
        

        if keys[pygame.K_SPACE]:
            if selected == 1:
                game.state = State.PLAY
                game.loadLevel(player)
            else:
                playing = False
        elif keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_w] or keys[pygame.K_s]:
            if selected == 1:
                selected = 2
            else:
                selected = 1

        menu_img = os.path.join(asset_path, 'menu-' + str(selected) +'.png')
        menu = pygame.image.load(menu_img)
        screen.blit(menu, (0,0))
        pygame.display.flip()



    elif game.state == State.PLAY:
            # before player update
        previous_x = player.rect.x
        previous_y = player.rect.y

        # player update 
        player.update()
        game.update()

        # check for collisions between player and walls
        wall_collisions = pygame.sprite.spritecollide(player, game.walls, False)
        for wall_collision in wall_collisions:

            # fall back to previous position
            player.rect.x = previous_x
            player.rect.y = previous_y
            break

        collectible_collisions = pygame.sprite.spritecollide(player, game.collectibles, False)
        for collectible in collectible_collisions:
            if collectible.name == "flag":
                pygame.mixer.Sound.play(win)
                game.level += 1
                if game.level >= len(levels):
                    game.state = State.GAME_OVER
                else:
                    game.loadLevel(player)
                pass
            else:
                collectible.collect(player)
            


        for projectile in game.projectiles:
            projectile_collisions = pygame.sprite.spritecollide(projectile, game.walls, False)
            for projectile_collision in projectile_collisions:
                if projectile_collision.color == projectile.color:
                    projectile_collision.kill()
                    projectile.kill()
                else:
                    projectile.kill()

        
        if keys[pygame.K_r]:
            game.loadLevel(player)
        if keys[pygame.K_ESCAPE]:
            game.state = State.MENU

        # draw
        screen.fill(BG_COLOR)

        # single sprites are drawn with screen.blit()
        screen.blit(player.image, (player.rect.x, player.rect.y))

        # groups of sprites can be drawn with group.draw()
        game.walls.draw(screen)
        game.collectibles.draw(screen)
        game.projectiles.draw(screen)

        ammo = my_font.render("R: " + str(player.bulletR)+ " G: " + str(player.bulletG) + " B: "+ str(player.bulletB) + "          [R]: restart  [Esc]: menu", False, (0, 0, 0))
        screen.blit(ammo, (0,0))

        pygame.display.flip()
        clock.tick(30)
    elif game.state == State.GAME_OVER:
        menu_img = os.path.join(asset_path, 'end.png')
        menu = pygame.image.load(menu_img)
        screen.blit(menu, (0,0))
        pygame.display.flip()

        if keys[pygame.K_ESCAPE]:
            playing = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False


pygame.quit()
sys.exit()