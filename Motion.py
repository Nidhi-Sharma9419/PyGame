# Initialize pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((1280, 720))

# Load image of ball
ball = pygame.image.load("ball.png") //Need to load an image in python directory first

# Set ball's initial position
x = 2       #I don't know how these values work
y = 0

# Set game clock
clock = pygame.time.Clock()

# Create game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update ball position
    x += 5
    y += 0

    # Draw ball on screen
    screen.blit(ball, (x, y))

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(120)
