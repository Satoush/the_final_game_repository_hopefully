'''
you will need to install:
pygame
math
random
'''
import time

import pygame
# from pygame.locals import *
import random
from character_class_v2 import Character
from Enemy import enemy
from Fast_Enemy import fast_enemy
from Button import button
from Tank_Enemy import tank_enemy

# Intialize pygame
pygame.init()
mx, my = pygame.mouse.get_pos()
font = pygame.font.SysFont("font/Pixeltype.ttf",75)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
screen = pygame.display.set_mode((800, 600))

########################################################################################
# Players data
playerX = 400
playerY = 300
rounds = 0
kills = 0
damage_taken = 0
image_dimensions_x = 48
image_dimensions_y = 26
last_update = pygame.time.get_ticks()
cooldown = 3000 # how fast the animation is
step_counter = 0


# Enemies data
Enemy_list = []
changeX  = 0
changeY = 0
velocity = 0.01
fast_velocity = 0.05
num_of_enemies = 6



# Player object
character = Character(playerX, playerY, mx, my,BLACK)

def spawn(num_of_enemies):
    count = 0
    while count < num_of_enemies:
        EnemyX = random.randint(0, 725)
        EnemyY = random.randint(0, 600)
        Enemy_pick = random.randint(0,2)
        if EnemyX <= (character.X + 128) and EnemyX >= (character.X - 128):
            if EnemyY <= (character.Y + 128) and EnemyY >= (character.Y - 128):
                pass
        else:
            if Enemy_pick == 0:
                zombie = enemy(pygame.image.load('Assets/zombie.png'),EnemyX, EnemyY,changeX,changeY)
                Enemy_list.append(zombie)
                count += 1
            elif Enemy_pick == 1:
                zombie_fast = fast_enemy(pygame.image.load('Assets/User_iconnn.png'), EnemyX, EnemyY, changeX, changeY)
                Enemy_list.append(zombie_fast)
                count += 1
            else:
                tough_zombie = tank_enemy(pygame.image.load('Assets/User_icon.png'), EnemyX, EnemyY, changeX, changeY)
                Enemy_list.append(tough_zombie)
                count += 1



character.draw_character()

image = (pygame.image.load('The_New_Assets/Character/static idle.png').convert_alpha())
# -------- Main Program Loop -----------

def main_menu():

    while True:
        mx,my = pygame.mouse.get_pos()
        screen.fill(BLACK)

        Play_Button = button(400,275,WHITE,font,'PLAY')
        Exit_Button = button(400, 500, WHITE, font, 'EXIT')

        for b in [Play_Button,Exit_Button]:
            b.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Button.pressed(mx,my):
                    game(rounds, kills,num_of_enemies, damage_taken, last_update, cooldown)
                if Exit_Button.pressed(mx,my):
                    pygame.quit()
                    exit()

        pygame.display.update()


def game(rounds,kills,num_of_enemies, damage_taken, last_update,  cooldown):
    running = True
    while running:

        # Background colour
        screen.fill(WHITE)
        character.animate_character(screen, BLACK)


        # Adding the exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_s\
                        or event.key == pygame.K_a or event.key == pygame.K_d:
                    character.current_sprite_sheet = 1
                    character.frame = 0
            else:
                if event.type == pygame.KEYUP:
                    character.current_sprite_sheet = 0
                    character.frame = 0


            # if event.type == pygame.K_DOWN or pygame.K_UP:
            #     character.current_sprite_sheet = 1
            #     character.frame = 0
                        # Fire button

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    character.frame = 0
                    character.current_sprite_sheet = 2
                    character.fire()

        for e in Enemy_list:
            if character.has_collided(e.rect) == True:
                character.current_sprite_sheet = 4
                character.frame = 0
                e.destroy(e, Enemy_list)
                current_time = pygame.time.get_ticks()  # takes the time the code is being executed
                if current_time - last_update >= cooldown:
                    running = False
                    spawn(1)
                # EnemyX = random.randint(0, 725)
                # EnemyY = random.randint(0, 600)
                # zombie = enemy(EnemyX, EnemyY)
                # Enemy_list.append(zombie)

        # Bullet list
        # tempList = character.bullets

        for bullet in character.bullets:
            bullet.draw(screen)
            bullet.move()
            for e in Enemy_list:
               if bullet.has_collided(e.rect):
                   bullet.destroy(bullet, character.bullets)
                   e.damage_taken += 1
                   if e.check_if_dead():
                       character.score += e.points
                       e.destroy(e,Enemy_list)
                       spawn(1)
                       kills +=1
                       print (character.score)

        if kills == num_of_enemies:
            kills = 0
            num = 0
            rounds += 1
            num_of_enemies += 1
            print ('round complete')
            spawn(num+1)



            #character.bullets = tempList
        enemy.updateAllZombies(Enemy_list,character.X,character.Y)
        # d
        # character.has_collided(zombie.rect)
        character.update()
        pygame.display.update()



spawn(1)

# Calling main program
main_menu()
#game(rounds,kills,num_of_enemies)