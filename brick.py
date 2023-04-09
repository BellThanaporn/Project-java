import pygame
BLACK = (0,0,0)

class Brick(pygame.sprite.Sprite):
    #This class represents a brick. 
    #It derives from the "Sprite" class in Pygame.


    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)


        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
        

       
