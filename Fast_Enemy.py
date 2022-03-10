from Enemy import enemy
import pygame
screen = pygame.display.set_mode((800, 600))

class fast_enemy(enemy):
    def __init__(self,Image_path,X,Y,changeX,changeY):
        enemy.__init__(self,Image_path,X,Y,changeX,changeY)
        self.Image_bath = Image_path
        self.points = 10
        self.velocity = 0.125
        self.health = 1

    # def draw(self):
    #     screen.blit(self.Image_path, (self.X , self.Y))
    #     #pygame.draw.rect(screen, pygame.Color("red"), (self.rect))

#pygame.image.load('Assets/zombie.png')