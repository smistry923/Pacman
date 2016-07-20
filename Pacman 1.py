import pygame
 
pygame.init()
 
screen = pygame.display.set_mode((700,500))


 
pygame.display.set_caption("Pacman")
 
black = (0,0,0)
white=(255,255,255)
 
x,y=0,0
 
moveX,moveY=0,0
 
clock = pygame.time.Clock()
 


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
DARKBLUE = (0,0,150)
PINK = (238,58,140)
YELLOW = (255,255,0)



# Set the width and height of the screen [width, height]



# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]


# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, ball_color, screen_width, screen_height):

        ball_color = ball_color # This is outside because of variable scoping.

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)

        
            



    	    

# -------- Main Program Loop -----------


ball = BouncingBall(350,250,5,10,30)
ball2 = BouncingBall(200,150,6,2,30)
ball3 = BouncingBall(100,300,3,5,30)
ball4 = BouncingBall(400,400,2,7,30)


gameLoop=True
while gameLoop:

    # --- Game logic should go here
   
   
 
    for event in pygame.event.get():
 
        if (event.type==pygame.QUIT):
 
            gameLoop=False
 
        if (event.type==pygame.KEYDOWN):
 
            if (event.key==pygame.K_LEFT):
 
                moveX = -5
 
            if (event.key==pygame.K_RIGHT):
 
                moveX = 5
 
            if (event.key==pygame.K_UP):
 
                moveY = -5
 
            if (event.key==pygame.K_DOWN):
 
                moveY = 5
 
        if (event.type==pygame.KEYUP):
 
            if (event.key==pygame.K_LEFT):
 
                moveX=0
 
            if (event.key==pygame.K_RIGHT):
 
                moveX=0
 
            if (event.key==pygame.K_UP):
 
                moveY=0
 
            if (event.key==pygame.K_DOWN):
 
                moveY=0

    screen.fill(BLACK)


    ball.flashBounce(screen,RED,700,500)
    ball2.flashBounce(screen,BLUE,700,500)
    ball3.flashBounce(screen,PINK,700,500)
    ball4.flashBounce(screen,YELLOW,700,500)


    x+=moveX
    y+=moveY

 
    pac = pygame.draw.circle(screen,YELLOW,(x,y), 50)

  
    
    






    pygame.display.update()

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


