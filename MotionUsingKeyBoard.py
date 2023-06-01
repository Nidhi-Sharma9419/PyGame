import pygame

pygame.init()

screen_width = 1280
screen_height = 720

BLACK = (0,0,0)
RED = (225, 0, 0)
#create screen
screen = pygame.display.set_mode([1280,720])



# Set the dimensions of the object
object_width = 50
object_height = 50

# Set the initial position of the object
object_x = 0   #Don't know how this is working?
object_y = 0

pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))

test = False
while not test:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                object_x = object_x-50
            if event.key == pygame.K_RIGHT:
                object_x = object_x+10
            if event.key == pygame.K_UP:
                object_y = object_y-10
            if event.key == pygame.K_DOWN:
                object_y = object_y+10
        screen.fill(BLACK)
        #crate rectangle
        surface = pygame.Surface([100,100])
        surface.fill(RED)
        rectangle=surface.get_rect()
        #give position of our rectangle
        rectangle.x=600
        rectangle.y = 400
        #move rectangle
        rectangle.x = rectangle.x+ object_x
        rectangle.y = rectangle.y + object_y
        #draw rectangle
        pygame.draw.rect(screen, RED, rectangle, 0)

        pygame.display.flip() 

pygame.quit()

'''if event.type == pygame.KEYDOWN:  
                key_input = pygame.key.   
                print(key_input[pygame.K_w], key_input[pygame.K_a], key_input[pygame.K_d])
            elif event.type == pygame.KEYUP:
                key_input = pygame.key.get_pressed()'''
