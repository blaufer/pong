import pygame

BLACK = (0,0,0)

#----------------------------------------------------------

class Paddle(pygame.sprite.Sprite):
    
    #------------------------------------------------------
    def __init__(self, color, width, height, ai=False, diff='easy'):
        # Initialize as a Sprite
        super().__init__()

        # AI
        self.ai = ai
        self.diff = diff
        self.impossible = False
        self.difficulty()

        # Draw the paddle
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Get the dimensions/location
        self.rect = self.image.get_rect()
    
    #------------------------------------------------------
    def difficulty(self):
        # Sets the difficulty of the AI based
        # on chosen option
        if self.diff == 'easy':
            self.m = 1
        elif self.diff == 'medium':
            self.m = 3
        elif self.diff == 'hard':
            self.m = 5
        elif self.diff == 'impossible':
            self.impossible = True
    
    #------------------------------------------------------
    def ai_update(self, ball):
        # Updates the paddle position if AI is True
        if self.impossible:
            self.rect.centery = ball.rect.centery
        else:
            if ball.rect.y < self.rect.y:
                self.moveUp(self.m)
            elif ball.rect.y > self.rect.y:
                self.moveDown(self.m)
    
    #------------------------------------------------------
    def moveUp(self, pixels):
        # Move the paddle up
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    #------------------------------------------------------
    def moveDown(self, pixels):
        # Move the paddle down
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400

#----------------------------------------------------------
