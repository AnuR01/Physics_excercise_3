# 2. Modify the code "Pygame_mass_spring_Euler.py" so that the simulation method 
# used is the same Verlet method that we used in the earlier code "Mass_spring_Verlet.py".

import pygame 
# Physical parameters
g = 10
k = 1
m = 1
L = 160

# Initailise Pygame
pygame.init()

# Screen size
width, height = 800, 600 
# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame intro")

# Create a clock 
FPS = 60
clock = pygame.time.Clock()

# Initail values
x_0 = width / 2
y_0 = height / 2
v_x_0 = 0
v_y_0 = 0
# Time step
dt = 0.01

# Initialise the variables
x = x_0
y = y_0
v_x = v_x_0
v_y = v_y_0


# Change the colour of the screen to yellow
screen.fill((255, 255, 255))

# Draw a line
pygame.draw.line(screen, (0, 255, 0), [width / 2, 0], [width / 2, height / 2], 10)

# Draw a circle
pygame.draw.circle(screen,(0, 0, 0),[width / 2, height / 2], 25)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill((255, 0, 0))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                     screen.fill((255, 255, 255))
              
       # Update the position and velocities of the objects

    a_x = g - k/m * (x - L) - 0.2 * v_x
    a_y = g - k/m * (x - L) - 0.2 * v_x
    x = x + dt * v_x+ 0.5 * dt**2 * a_y
    v_x = v_x+ dt * a_y
    v_y = v_y + dt * (a_x+ a_y) / 2
   



    # Update the screen
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 255, 0), [width / 2, 0], [x, y], 10)
    pygame.draw.circle(screen, (0, 0, 0), [x, y], 25)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
