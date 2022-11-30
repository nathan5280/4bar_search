# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([200 * 5, 120 * 5])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case unknown_command:
                print(event)

    # Fill the background with white
    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (0, 0, 128), (0, 0), (100 * 5, 100 * 5))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
