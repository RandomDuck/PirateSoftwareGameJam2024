import pygame
from scripts.ui_controller import UiController as UICon

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 1080))
clock = pygame.time.Clock()
running = True

# Set variables
UiController = UICon(screen)

# Event handleing
def fetchEvents():
  events = []
  for event in pygame.event.get():
      events.append(event.type)
  return events

# Game setup
def setup():  
  UiController.setup()

setup()
while running:
    # poll for events
    events = fetchEvents()
    # pygame.QUIT event means the user clicked X to close your window
    if pygame.QUIT in events:
        running = False

    # Fill the window with black
    screen.fill((0, 0, 0))

    # Render game controllers
    UiController.render(events)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()