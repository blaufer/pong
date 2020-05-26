import pygame
from random import randint, choice

BLACK = (0,0,0)

#----------------------------------------------------------

class Ball(pygame.sprite.Sprite):
    
    #------------------------------------------------------
    def __init__(self, color, width, height):
        # Initialize as a Sprite
        super().__init__()

        # Draw the ball
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Set initial velocity (speed and direction)
        self.velocity = [choice([-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]), \
            randint(-8,8)]
        
        # Get the dimensions/location
        self.rect = self.image.get_rect()

    #------------------------------------------------------
    def update(self):
        # Update the position
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    #------------------------------------------------------
    def bounce(self):
        # Bounce off the paddle with random y velocity
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    #------------------------------------------------------
    def destroy(self):
        # Destroy the object. Happens if
        # the left or right wall is hit
        self.kill()

#----------------------------------------------------------
