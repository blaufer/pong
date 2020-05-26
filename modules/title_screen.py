import pygame

# Setup colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#----------------------------------------------------------

class TitleScreen():
    
    #------------------------------------------------------
    def __init__(self, screen, carryOn):
        self.screen = screen
        self.carryOn = carryOn
        
        self.ai = False
        self.diff = 'easy'

        self.start()
        
    #------------------------------------------------------
    def start(self):
        while self.carryOn:
            # Quit if closed or x is pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.carryOn = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.carryOn = False

            self.screen.fill(BLACK)

            # Place the title
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 75)
            text = font.render('PONG', 1, WHITE)
            text_rect = text.get_rect(center=(350,150))
            self.screen.blit(text, text_rect)

            # Place the Player 1 controls
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
            text = font.render('Player 1 Controls', 1, WHITE)
            self.screen.blit(text, (10,10))
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
            text = font.render('w = Move Up', 1, WHITE)
            self.screen.blit(text, (10,30))
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
            text = font.render('s = Move Down', 1, WHITE)
            self.screen.blit(text, (10,50))
            
            # Place the Player 2 controls
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
            text = font.render('Player 2 Controls', 1, WHITE)
            self.screen.blit(text, (540,10))
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
            text = font.render('UP = Move Up', 1, WHITE)
            self.screen.blit(text, (540,30))
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
            text = font.render('DOWN = Move Down', 1, WHITE)
            self.screen.blit(text, (540,50))

            # Place the 1 Player button
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 50)
            text = font.render('1 Player', 1, WHITE)
            text_rect = text.get_rect(center=(175,350))
            b1 = self.screen.blit(text, text_rect)

            # Place the 2 Player button
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 50)
            text = font.render('2 Player', 1, WHITE)
            text_rect = text.get_rect(center=(525,350))
            b2 = self.screen.blit(text, text_rect)
            
            pygame.display.flip()

            # Detect key press
            self.keys = pygame.key.get_pressed()

            # If the either 1 or 2 Player is clicked on,
            # move to the difficulty screen then countdown
            # or straight to the countdown
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # 1 Player chosen so AI started
                if b1.collidepoint(pos):
                    self.ai = True
                    self.difficulty()
                    self.countdown()
                    return
                elif b2.collidepoint(pos):
                    self.ai = False
                    self.countdown()
                    return

            # If enter key is pressed, start 1 Player
            # option then go to the difficulty screen
            # and then the countdown
            if self.keys[pygame.K_RETURN]:
                self.ai = True
                self.difficulty()
                self.countdown()
                return

    #------------------------------------------------------
    def difficulty(self):
        # Creates the difficulty screen if
        # 1 Player is chosen
        while self.carryOn:
            # Quit if closed or x is pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.carryOn = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.carryOn = False
            
            # Draw background of screen
            self.screen.fill(BLACK)
            
            # Easy Medium Hard buttons
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
            text = font.render('Easy', 1, WHITE)
            text_rect = text.get_rect(center=(340,100))
            b1 = self.screen.blit(text, text_rect)
            
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
            text = font.render('Medium', 1, WHITE)
            text_rect = text.get_rect(center=(340,200))
            b2 = self.screen.blit(text, text_rect)
            
            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
            text = font.render('Hard', 1, WHITE)
            text_rect = text.get_rect(center=(340,300))
            b3 = self.screen.blit(text, text_rect)

            font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
            text = font.render('Impossible', 1, WHITE)
            text_rect = text.get_rect(center=(340,400))
            b4 = self.screen.blit(text, text_rect)
            
            pygame.display.flip()

            # Detect key press
            self.keys = pygame.key.get_pressed()

            # Set difficulty based on button clicked
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if b1.collidepoint(pos):
                        self.difficulty = 'easy'
                        return
                    elif b2.collidepoint(pos):
                        self.diff = 'medium'
                        return
                    elif b3.collidepoint(pos):
                        self.diff = 'hard'
                        return
                    elif b4.collidepoint(pos):
                        self.diff = 'impossible'
                        return
                
                # REMOVED because pressing enter on 
                # start screen causes this to occur too
                '''
                # If enter key is pressed, set as easy
                if self.keys[pygame.K_RETURN]:
                    self.diff = 'easy'
                    return
                '''

    #------------------------------------------------------
    def countdown(self):
        # Starts a countdown screen before
        # the game starts
        font = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 75)

        for i in range(3,0,-1):
            self.screen.fill(BLACK)
            text = font.render(str(i), 1, WHITE)
            text_rect = text.get_rect(center=(350,250))
            self.screen.blit(text, text_rect)

            pygame.display.flip()

            pygame.time.wait(1000)
        
        return 

#----------------------------------------------------------
