import pygame

class button():
    def __init__(self, pos_X, pos_Y, colour, font, word):
        #self.image = pygame.image.load('Assets/Button_background.png')
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.colour = colour
        self.font = font
        self.word = word
        #self.rect = self.image.get_rect(center=(400, 300))
        self.text = font.render(word,True,self.colour)
        self.text_rect = self.text.get_rect(center = (self.pos_X,self.pos_Y))

    def draw(self,screen):
        screen.blit(self.text,self.text_rect)
        #screen.blit(self.image, self.rect)

    def pressed(self, mx,my):
        if mx in range(self.text_rect.left, self.text_rect.right) and my in range(self.text_rect.top,
                                                                                          self.text_rect.bottom):
            return True
        return False