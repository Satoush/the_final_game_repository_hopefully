import pygame
from Bullet_v2 import bullet
import math

screen = pygame.display.set_mode((800, 600))

class Character():
    def __init__(self,X,Y,changeX,changeY,targetY,targetX):
        super().__init__()
        self.image = pygame.image.load('Assets/User_icon.png')
        self.X = X
        self.Y = Y
        self.changeX = changeX
        self.changeY = changeY
        self.velocity = 0.5
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


    def draw_character(self):

        mx, my = pygame.mouse.get_pos()

        dist_X = mx - self.X
        dist_Y = my - self.Y

        angle = math.atan2(dist_X, dist_Y)  * (180 / math.pi)

        rotated_image = pygame.transform.rotate(self.image, angle)
        #pygame.draw.line(screen, pygame.Color("red"), (self.X, self.Y), (mx, my))
        screen.blit(rotated_image, (self.X,self.Y))
        # pygame.draw.rect(screen,"red" , (self.rect))

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
        self.draw_character()
