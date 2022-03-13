import pygame
from Bullet_v2 import bullet
import math

# screen = pygame.display.set_mode((800, 600))

class Character():
    def __init__(self,X,Y,targetY,targetX,colour):
        self.sprite_sheets = []
        self.sprite = [] # holds individual sprites
        self.image = pygame.image.load('Assets/User_icon.png').convert_alpha()
        self.sprite_sheets.append(pygame.image.load('The_New_Assets/Character/static idle.png').convert_alpha()) #0
        self.sprite_sheets.append(pygame.image.load('The_New_Assets/Character/move without FX.png').convert_alpha())
        self.sprite_sheets.append(pygame.image.load('The_New_Assets/Character/shoot without FX.png').convert_alpha())
        self.sprite_sheets.append(pygame.image.load('The_New_Assets/Character/damaged.png').convert_alpha())
        self.sprite_sheets.append(pygame.image.load('The_New_Assets/Character/death.png').convert_alpha())
        self.current_sprite_sheet = 0 # gets the current sprite sheet from the list
        self.last_update = pygame.time.get_ticks()

        self.animation_stage = 0
        self.animation_steps = [1,8,4,2,6]
        self.current_state = 0
        self.rect = self.image.get_rect(topleft =(400, 300))
        #self.new_image =



        self.width = 48
        self.height = 26
        self.cooldown = 100
        self.frame = 0
        self.step_counter = 0
        self.scale = 3
        self.colour = colour

        self.X = X
        self.Y = Y
        self.changeX = 0
        self.changeY = 0
        self.velocity = 0.25
        self.bullets = []
        self.bullet_vel = 10
        self.targetX = targetX
        self.targetY = targetY
        self.angle = math.atan2(targetY - Y, targetY - X)
        self.dx = math.cos(self.angle) * self.velocity
        self.dy = math.sin(self.angle) * self.velocity
        self.rect = self.image.get_rect(topleft=(400, 300))
        self.score = 0


    def player_input(self):
        key = pygame.key.get_pressed()
        self.changeX = 0
        self.changeY = 0
        if key[pygame.K_DOWN] or key[pygame.K_UP] or key[pygame.K_w] or key[pygame.K_s]:
            self.changeY = self.velocity * - (int(key[pygame.K_UP] or key[pygame.K_w]) * 2 - 1)




        if key[pygame.K_LEFT] or key[pygame.K_RIGHT] or key[pygame.K_a] or key[pygame.K_d]:
            self.changeX = self.velocity * - (int(key[pygame.K_LEFT] or key[pygame.K_a]) * 2 - 1)



        self.X += self.changeX
        self.Y += self.changeY

        self.rect[0] = self.X
        self.rect[1] = self.Y

    def get_image(self, frame_of_image, width, height, scale,colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sprite_sheets[self.current_state - 1],(0,0), (0, (frame_of_image * height), width, height))
        image = pygame.transform.scale(image,(width * scale, height * scale))
        image.set_colorkey(colour)

        return image


    def draw_character(self):
        for animation in self.animation_steps:
            temp_list = []
            self.current_state += 1
            for i in range(animation):
                temp_list.append(self.get_image(self.step_counter, self.width, self.height, 3, self.colour))
                self.step_counter += 1
            self.step_counter = 0
            self.sprite.append(temp_list)


    def animate_character(self,screen,colour):
        #Update, this is where the character get animated
        current_time = pygame.time.get_ticks()  # takes the time the code is being executed
        if current_time -  self.last_update  >= self.cooldown:
            self.frame += 1
            self.last_update = current_time  # resets the cooldown
            if self.current_sprite_sheet == 2 or self.current_sprite_sheet == 3 or self.current_sprite_sheet == 4:
                self.frame = len(self.sprite[self.current_sprite_sheet]) - 1
            elif self.frame >= len(self.sprite[self.current_sprite_sheet]):  # makes sure the list doesnt go out of range
                self.frame = 0

        mx, my = pygame.mouse.get_pos()
        dist_X = mx - self.X
        dist_Y = my - self.Y

        angle = math.atan2(dist_X, dist_Y)  * (180 / math.pi)


        if angle <= 0:
            flipped_image = pygame.transform.flip(self.sprite[self.current_sprite_sheet][self.frame], True, False)
            flipped_image.set_colorkey(colour)
            new_image = flipped_image
        else:
            image = self.sprite[self.current_sprite_sheet][self.frame]
            new_image = image



        # Show frame image
        screen.blit(new_image,(self.X, self.Y))



        # self.frame_of_image += 1
        # rotated_image = pygame.transform.rotate(self.image, angle)
        # #pygame.draw.line(screen, pygame.Color("red"), (self.X, self.Y), (mx, my))
        # screen.blit(rotated_image, (self.X,self.Y))
        #pygame.draw.rect(screen,"red" , (self.rect))

    def boundaries(self):
        if self.X <= 0:
            self.X = 0
            self.rect[0] = 0

        elif self.X >= 750:
            self.X = 750
            self.rect[0] = 750


        if self.Y <= 0:
            self.Y = 0
            self.rect[1] = 0

        elif self.Y >= 555:
            self.Y = 555
            self.rect[1] = 555



    def fire(self):
        mx, my = pygame.mouse.get_pos()
        new_bullet = bullet('Assets/Bullet.png',(255, 0, 0),self.X+16,self.Y+16,self.bullet_vel,mx,my)
        new_bullet.move()
        self.bullets.append(new_bullet)
        print('fire')

    def has_collided(self,Enemy):
        if self.rect.colliderect(Enemy):
            return True

    def count_score(self,points):
        self.score += points
        return self.score

    #
    #     rect = Enemy.rect
    #     if self.X > Enemy.X and self.X < rect[2] + Enemy.X:
    #         if self.Y > Enemy.Y and self.Y < rect[3] + Enemy.Y:
    #             return True
    #
    #     return False


    def update(self):
        self.player_input()
        self.boundaries()
        #self.draw_character()