import pygame
from scripts.ui_controller import UiController as UICon
from scripts.game_controller import GameCon
from scripts.modules.settings import Settings
from scripts.components.utils import setGameIcon, fetchEvents, setGameName, SplashScreen, timedEvents

# pygame setup
pygame.init()
aspect = (720, 1080)
screen = pygame.display.set_mode(aspect)
clock = pygame.time.Clock()
running = True

# Set globals
SplScr = SplashScreen(screen, 2)
gameCon = GameCon()
UiController = UICon(screen, gameCon)
settingCollors = ((160,160,160),(127,255,127))
SettingCon = Settings(screen, (200,30), settingCollors, (0,0,255), UiController.setClickable)
updateFPS = timedEvents(1,gameCon.useFPS)

# Game setup
def setup():
  # Set game data
  setGameIcon()
  setGameName()

  # Setup controllers
  UiController.setup()
  SettingCon.setup()

def update():
   UiController.update()
   SettingCon.update()
   if SplScr.shouldDisplaySplash():
      SplScr.update()

def hande_options():
  # handle aspect ratio change
  newAspect = SettingCon.getAspect()
  global aspect
  if aspect != newAspect:
      aspect = newAspect
      pygame.display.set_mode(aspect)
      update()
#TODO: Save Load and Reset functions
#TODO: store items increments in cost
#TODO: store items display ammount owned
#TODO: Generate random fake news and posts in quacker and news
#TODO: make profile display recent posts
#TODO: icons for items
#TODO: improve UI
setup()
while running:
    # poll for events
    events = fetchEvents()
    # pygame.QUIT event means the user clicked X to close your window
    if pygame.QUIT in events:
        # TODO: save game here too
        running = False
        
    updateFPS.updateEvent()
    # check if we need to handle options
    hande_options()
    # Fill the window with teal
    screen.fill((0, 100, 100))

    # Render splash screen
    if SplScr.shouldDisplaySplash():
      SplScr.render()
    else:
      # Render game controllers
      UiController.render(events)
      SettingCon.render(events)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()