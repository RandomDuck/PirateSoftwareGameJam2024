import pygame
from scripts.ui_controller import UiController as UICon
from scripts.modules.settings import Settings

# pygame setup
pygame.init()
aspect = (720, 1080)
screen = pygame.display.set_mode(aspect)
clock = pygame.time.Clock()
running = True

# Set variables
UiController = UICon(screen)
settingCollors = ((160,160,160),(127,255,127))
SettingCon = Settings(screen, (200,30), settingCollors, (0,0,255))

# Event handleing
def fetchEvents():
  events = []
  for event in pygame.event.get():
      events.append(event.type)
  return events

# Game setup
def setup():
  # Set game icon
  image_path = "resources/icon.jpg"
  icon_image = pygame.image.load(image_path)
  icon_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
  icon_image = pygame.transform.scale(icon_image, (32, 32))
  icon_surface.blit(icon_image, (0, 0))
  pygame.display.set_icon(icon_surface)

  # Setup controllers
  UiController.setup()
  SettingCon.setup()

def update():
   UiController.update()
   SettingCon.update()

def hande_options():
  # handle aspect ratio change
  newAspect = SettingCon.getAspect()
  global aspect
  if aspect != newAspect:
      aspect = newAspect
      pygame.display.set_mode(aspect)
      update()

setup()
while running:
    # poll for events
    events = fetchEvents()
    # pygame.QUIT event means the user clicked X to close your window
    if pygame.QUIT in events:
        running = False

    # check if we need to handle options
    hande_options()
    # Fill the window with teal
    screen.fill((0, 100, 100))

    # Render game controllers
    UiController.render(events)
    SettingCon.render(events)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()