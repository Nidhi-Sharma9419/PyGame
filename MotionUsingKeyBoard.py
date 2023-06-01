import pygame
import websocket
from pygame.event import Event
import threading

pygame.init()
screen_width = 1280
screen_height = 720
BLACK = (0,0,0)
RED = (225, 0, 0)

#create screen
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the dimensions of the object
object_width = 50
object_height = 50

# Set the initial position of the object
object_x = 0
object_y = 0

rectangle = pygame.Surface([object_height, object_width]).fill(RED)
rectangle.x = object_x
rectangle.y = object_y

test = False

#Custom Events
move_up = pygame.event.custom_type()
move_down = pygame.event.custom_type()
move_left = pygame.event.custom_type()
move_right = pygame.event.custom_type()

def on_message(wsapp, message):
    if(message == 'w'):
        pygame.event.post(Event(move_up))
    if(message == 's'):
        pygame.event.post(Event(move_down))
    if(message == 'a'):
        pygame.event.post(Event(move_left))
    if(message == 'd'):
        pygame.event.post(Event(move_right))

# websocket.enableTrace(True)
wsapp = websocket.WebSocketApp("ws://192.168.153.239:3000/game", on_message=on_message)
wsapp_thread = threading.Thread(target=wsapp.run_forever)
wsapp_thread.daemon = True
wsapp_thread.start()

while not test:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test = True
        elif event.type == move_left:
            rectangle.x = rectangle.x - 10
        elif event.type == move_right:
            rectangle.x = rectangle.x + 10
        elif event.type == move_up:
            rectangle.y = rectangle.y - 10
        elif event.type == move_down:
            rectangle.y = rectangle.y + 10
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, rectangle, 0)
        pygame.display.flip()

pygame.quit()
