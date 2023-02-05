# 1. Modify the code "Pygame_test.py" so that
#The width of the window is 800
#pixels and the height is 600 pixels.
#When you press the "y" key on the keyboard, the circle on the screen turns yellow.
#It should stay yellow even after you let go of the key.
#EXTRA: When you click somewhere inside the window with the mouse, a new circle appears there.

import pygame

# Initialize Pygame
pygame.init()

# Screen size
width, height = 800, 600

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame intro")

# Change the color of the screen
screen.fill((255, 255, 255))

# Draw a circle
pygame.draw.circle(screen, (0, 0, 0), [width / 2, height / 2], 25)

# Draw a line
pygame.draw.line(screen, (0, 255, 0), [width / 2, 0], [width / 2, height / 2], 10)

# Game loop
running = True
key_press = False
while running:
    # Handle all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                key_press = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0, 0, 0), pos, 25)
    
    # Update the positions and velocities of the objects
    # ....

    # Update the screen
    if key_press:
        pygame.draw.circle(screen, (255, 255, 0), [width / 2, height / 2], 25)
    else:
        pygame.draw.circle(screen, (0, 0, 0), [width / 2, height / 2], 25)
    pygame.draw.line(screen, (0, 255, 0), [width / 2, 0], [width / 2, height / 2], 10)
    pygame.display.update()
