# PyGame

1. Introduction
How to install pygame and what are the basic syntax that are used while using pyGame.
In Pygame, you typically use a game loop to keep your game running and update its state. The game loop consists of three main parts:

Event handling: This involves handling user input events such as mouse clicks, keyboard presses, and gamepad events. Pygame provides an event queue that you can check for new events and respond to them appropriately.

Updating the game state: This involves updating the state of your game, including the positions of game objects, scorekeeping, and other game logic. You typically do this in response to user input or based on the passage of time.

Rendering: This involves drawing the updated game state on the screen. You can use Pygame's graphics functions and modules to draw shapes, images, and text on the screen.

"pygame.event.get()":-
In Pygame, the event queue is a buffer that stores all the input events generated by the user, such as mouse clicks, keyboard presses, and gamepad events. You can retrieve the events from the queue using the 'pygame.event.get()' function, which returns a list of all the events that have occurred since the last time the function was called.

"pygame.math" :-
  pygame module for vector classes
1. pygame.math.clamp
2. returns value clamped to min and max.
3. pygame.math.lerp
4. interpolates between two values by a weight.
5. pygame.math.Vector2
6. a 2-Dimensional Vector
7. pygame.math.Vector3
8. a 3-Dimensional Vector

"pygame.draw" module:-
1. Pygame.draw is a module in the Pygame library that provides functions to draw basic shapes like lines, rectangles, circles, and polygons on a Pygame surface.
