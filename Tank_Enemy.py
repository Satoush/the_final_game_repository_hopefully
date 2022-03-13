from Enemy import enemy
import pygame
screen = pygame.display.set_mode((800, 600))

class tank_enemy(enemy):
    def __init__(self,Image_path,X,Y,changeX,changeY):
        enemy.__init__(self,Image_path,X,Y,changeX,changeY)
        self.Image_bath = Image_path
        self.points = 15
        self.health = 3
        self.velocity = 0.025

    def check_if_dead(self):
        if self.damage_taken == self.health:
            return True

    def destroy(self,enemy_object, enemy_array):
        if enemy_object in enemy_array:
                print ('tank destroyed')
                enemy_array.remove(self)
                del self
