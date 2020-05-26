import pygame
from modules.title_screen import TitleScreen
from modules.paddle import Paddle
from modules.ball import Ball

# Setup colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#----------------------------------------------------------

class Pong(TitleScreen, Ball, Paddle):

    #------------------------------------------------------
    def __init__(self):
        pygame.init()

        # Setup the screen
        size = (700,500)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Pong')
        
        # Set to continue until X in right hand
        # upper corner pressed or the key x is
        # pressed
        self.carryOn = True

        # Start screen setup
        ts = TitleScreen(self.screen, self.carryOn)
        self.carryOn = ts.carryOn
        
        # Initial ball
        self.ball = Ball(WHITE, 10, 10)
        self.ball.rect.x = 345
        self.ball.rect.y = 195

        # Player 1 paddle (left side)
        self.paddleA = Paddle(WHITE, 10, 100)
        self.paddleA.rect.x = 20
        self.paddleA.rect.y = 200

        # Player 2 paddle (right side)
        self.paddleB = Paddle(WHITE, 10, 100, ts.ai, ts.diff)
        self.paddleB.rect.x = 670
        self.paddleB.rect.y = 200

        # Group all the sprites
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.ball)
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)

        # Setup the clock for smooth runnning
        self.clock = pygame.time.Clock()

        # Initial scores
        self.scoreA = 0
        self.scoreB = 0
        
        # Run the game
        self.main()
    
    #------------------------------------------------------
    def main(self):
        # Main loop to run the game
        while self.carryOn:
            # Quit if closed or x is pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.carryOn = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.carryOn = False
            
            # Capture key presses
            self.keys = pygame.key.get_pressed()
            # w moves paddle 1 up
            if self.keys[pygame.K_w]:
                self.paddleA.moveUp(5)
            # s moves paddle 1 down
            if self.keys[pygame.K_s]:
                self.paddleA.moveDown(5)
            if not self.paddleB.ai:
                # UP moves paddle 2 up
                if self.keys[pygame.K_UP]:
                    self.paddleB.moveUp(5)
                # DOWN moves paddle 2 down
                if self.keys[pygame.K_DOWN]:
                    self.paddleB.moveDown(5)
            else:
                # AI for paddle 2
                self.paddleB.ai_update(self.ball)  

            # Game logic
            self.all_sprites_list.update()
            
            # If ball hits wall, what happens?
            # Ball at far right wall
            if self.ball.rect.x >= 690:
                self.scoreA += 1
                # Destroy the ball and restart it at the center
                self.ball.destroy()
                self.ball = Ball(WHITE, 10, 10)
                self.ball.rect.x = 345
                self.ball.rect.y = 195
                self.all_sprites_list.add(self.ball)
            # Ball at far left wall
            if self.ball.rect.x <= 0:
                self.scoreB += 1
                # Destroy the ball and restart it at the center
                self.ball.destroy()
                self.ball = Ball(WHITE, 10, 10)
                self.ball.rect.x = 345
                self.ball.rect.y = 195
                self.all_sprites_list.add(self.ball)
            # Ball at top wall
            if self.ball.rect.y > 490:
                self.ball.velocity[1] = -self.ball.velocity[1]
            # Ball at bottom wall
            if self.ball.rect.y < 0:
                self.ball.velocity[1] = -self.ball.velocity[1]
            
            # Detect a collision between ball and paddle
            if pygame.sprite.collide_mask(self.ball, self.paddleA) \
                or pygame.sprite.collide_mask(self.ball, self.paddleB):
                self.ball.bounce()
            
            # Draw/Update the screen
            self.screen.fill(BLACK)
            pygame.draw.line(self.screen, WHITE, [349,0], \
                [349, 500], 5)

            self.all_sprites_list.draw(self.screen)

            # Add the score to the top of the screen
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 36)
            text = font.render(str(self.scoreA), 1, WHITE)
            self.screen.blit(text, (250, 10))
            text = font.render(str(self.scoreB), 1, WHITE)
            self.screen.blit(text, (420, 10))

            pygame.display.flip()

            # Update the screen every 60 milliseconds
            self.clock.tick(60)

        # Cleanly exit the game
        pygame.quit()

#----------------------------------------------------------

if __name__ == '__main__':
    Pong()
