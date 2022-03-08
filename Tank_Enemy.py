from Enemy import enemy
import pygame
screen = pygame.display.set_mode((800, 600))

class tank_enemy(enemy):
    def __init__(self,Image_path,X,Y,changeX,changeY,velocity):
        enemy.__init__(self,Image_path,X,Y,changeX,changeY,velocity)
        self.Image_bath = Image_path
        self.points = 10
        self.ttk = 3
        self.velocity = 0.025

    def destroy(self,enemy_object, enemy_array,damage):
        if damage == self.ttk:
            if enemy_object in enemy_array:
                    print ('tank destroyed')
                    enemy_array.remove(self)
                    del self
