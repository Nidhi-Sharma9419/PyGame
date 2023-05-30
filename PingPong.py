import pygame, sys

'''What's imp
Movement
Control
Collision Detection
Scoring
AI'''

'''Divide and conquer'''

'''vARIABLES, OBJECTS

uPDATING POSITIONS'
Checking for collision'''

def animate_bally():
    global bally_speed_x, bally_speed_y
    bally.x+= bally_speed_x   #this will increase each by pixel
    bally.y+= bally_speed_y

    if bally.bottom >= screen_height or bally.top<= 0:
        bally_speed_y *= -1

    if bally.right >= screen_width or bally.left <= 0:
        bally_speed_x *= -1


pygame.init()



screen_width = 1280
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
#Giving title
pygame.display.set_caption("My Pong Game")

#Getting clock object to control the frame rate of the game, how fast the game will run.
clock = pygame.time.Clock()

'''Definitions part completed'''
BLACK = (0,0,0)
RED = (225, 0, 0)
#create screen
#screen = pygame.display.set_mode([1280,720])



# Set the dimensions of the object
object_width = 30
object_height = 30

# Set the initial position of the object
object_x = 0  
object_y = 0

bally= pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))
bally.center= (screen_width/2, screen_height/2)


cpu = pygame.Rect(0,0,20,100)
cpu.centery = screen_height/2

player = pygame.Rect(0,0,20,100)
player.midright = (screen_width, screen_height/2)

bally_speed_x = 6
bally_speed_y = 6


'''Now GAME LOOP part''' 
#Check for events
#Update the positions of the game objects
#Draw the game objects and update the screen

while True:
    for event in pygame.event.get():#This line gets all the events that pygame recognizes and happened since the last time the while loop ran and puts them in a list
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        animate_bally()    

        '''bally.x+= bally_speed_x   #this will increase each by pixel
        bally.y+= bally_speed_y

        if bally.bottom >= screen_height or bally.top<= 0:
            bally_speed_y *= -1

        if bally.right >= screen_width or bally.left <= 0:
            bally_speed_x *= -1'''
        
    #Draw game objects
        screen.fill(BLACK) #does not leave mark when object moves
    #crate rectangle
        surface = pygame.Surface([100,100])
        surface.fill(RED)
        rectangle=surface.get_rect()
    #give position of our rectangle
        rectangle.x=640
        rectangle.y = 300
    
    #draw rectangle
        pygame.draw.aaline(screen, 'white', (screen_width/2,0), (screen_width/2, screen_height))
        pygame.draw.ellipse(screen, RED, bally)

        pygame.draw.rect(screen, 'white', cpu)
        pygame.draw.rect(screen, 'white', player)
        pygame.display.flip()     
    #Update the diplay
    pygame.display.update

    #Now we need to tell the object how fast it should run
    #that's why we will use tick() function
    #It takes an integer as an argument an that integer is the number of frames per second that we want
    clock.tick(60)


    #How to draw things on the surface
    
    
    
        

