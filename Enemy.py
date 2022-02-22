import pygame
import random

screen = pygame.display.set_mode((800, 600))


class enemy():
    def __init__(self,X,Y):
        self.Image_path = pygame.image.load('Assets/zombie.png')
        self.X = X
        self.Y = Y
        self.velocity = 0.01
        self.num_of_enemies = 6
        self.rect = self.Image_path.get_rect(center = (self.X,self.Y))
       #print(self.rect)



    def draw(self):
        screen.blit(self.Image_path, (self.X , self.Y))
        #pygame.draw.rect(screen, pygame.Color("red"), (self.rect))

    # Adding basic movement towards player
    def move_to_player(self, PlayerX,PlayerY):
        if self.X > PlayerX:
            self.changeX =  -1 * self.velocity

        elif self.X < PlayerX:
            self.changeX = self.velocity

        else:
            if self.Y == PlayerX:
                self.changeX = 0


        if self.Y > PlayerY:
            self.changeY =  -1 * self.velocity

        elif self.Y < PlayerY:
            self.changeY = self.velocity

        else:
            if self.Y == PlayerY:
                self.changeY = 0

        self.rect[0] = self.X
        self.rect[1] = self.Y




        self.X += self.changeX
        self.Y += self.changeY

            # self.rect[1] += self.changeY
            # self.rect[0] += self.changeX


    def destroy(self,Enemy_array):
        Enemy_array.remove(self)
        del self

    


    def update(self,PlayerX,PlayerY):
        self.move_to_player(PlayerX,PlayerY)
        self.draw()



    @staticmethod
    def updateAllZombies(Enemy_list,PlayerX,PlayerY):
        for e in Enemy_list:
            e.update(PlayerX,PlayerY)


