import pygame
import math

screen = pygame.display.set_mode((800, 600))


class bullet():
    def __init__(self,Image_path,colour ,pos_X, pos_Y,velocity,mx,my):
        self.Image_path = Image_path
        self.image = pygame.image.load(Image_path)
        self.rect = self.image.get_rect(center=(400, 300))
        self.colour = colour
        self.posX = pos_X
        self.posY = pos_Y
        self.velocity = velocity
        ##################################################
        self.angle = math.atan2(my - pos_Y, mx - pos_X)
        self.dx = math.cos(self.angle) * velocity
        self.dy = math.sin(self.angle) * velocity
       # players x and z`


    def move(self):
        self.posX += self.dx
        self.posY += self.dy
        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)


    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)
        rotated_image = pygame.transform.rotate(self.image, self.angle)  # This changes the rotation of the players image where the position of the mouse would be
        screen.blit(rotated_image, (self.posX, self.posY))

    def destroy(self,bullet_object,bullet_array):
        if bullet_object in bullet_array:
            bullet_array.remove(self)
            del self

    def has_collided(self, Enemy):
        if self.rect.colliderect(Enemy):
            return True


    # def update(self):
    #     self.move()
    #     self.destroy()














