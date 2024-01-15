import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 1080))
clock = pygame.time.Clock()
running = True
x, y = 50, 50

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the mouse position
    mouseX, mouseY = pygame.mouse.get_pos()

    # Check if the left mouse button is pressed
    if pygame.mouse.get_pressed()[0]:
        x, y = mouseX, mouseY

    screen.fill((0, 0, 0))  # Fill the window with black
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))  # Draw a red rectangle


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()