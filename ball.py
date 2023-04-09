import pygame
from random import randint

BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a car. 
    #It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height]) 
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height]) 
        
        self.vel = [randint(4,8),randint(-8,8)] 
        self.rect = self.image.get_rect() 
        
    def update(self): 
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
          
    def bounce(self): 
        self.vel[0] = -self.vel[0]
        self.vel[1] = -self.vel[1]

