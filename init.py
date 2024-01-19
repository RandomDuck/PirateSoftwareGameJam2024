import pygame
import scripts.components.button as btn

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 1080))
clock = pygame.time.Clock()
running = True
x, y = 50, 50

button = btn.TextButton((20,20), "Hello world", (screen.get_rect().width-40,50), ((255,255,255),(255,127,127)), (255,0,0), (True, True))

while running:
    triggerMouseEvents = False
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            triggerMouseEvents = True
    
    # Get the mouse position
    mouseX, mouseY = pygame.mouse.get_pos()

    # Check if the left mouse button is pressed
    if pygame.mouse.get_pressed()[0]:
        x, y = mouseX, mouseY

    screen.fill((0, 0, 0))  # Fill the window with black
    button.render(screen, triggerMouseEvents)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 5, 5))  # Draw a red rectangle


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()