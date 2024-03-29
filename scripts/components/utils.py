import pygame
import os
import sys

def setGameIcon():
  # Set game icon
  image_path = resource_path("resources/icon.png")
  image_width, image_height = (128,128)
  icon_image = pygame.image.load(image_path)
  icon_image = pygame.transform.scale(icon_image, (image_width,image_height))

  # Create a surface with per-pixel alpha
  image_surface = pygame.Surface((image_width, image_height), pygame.SRCALPHA)

  # Draw the image onto the alpha surface
  image_surface.blit(icon_image, (0, 0))

  # Create a circular mask
  mask_radius = min(image_width, image_height) // 2
  mask = pygame.Surface((mask_radius * 2, mask_radius * 2), pygame.SRCALPHA)
  pygame.draw.circle(mask, (255, 255, 255, 255), (mask_radius, mask_radius), mask_radius)

  # Apply the circular mask to the image surface
  image_surface.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
  pygame.display.set_icon(image_surface)

def setGameName():
   title = 'Viral Hysteria'
   pygame.display.set_caption(title, title)

# Event handleing
def fetchEvents():
  events = []
  for event in pygame.event.get():
      events.append(event.type)
  return events

class timedEvents:
  def __init__(self, wait, trigger=lambda:print("Triggerd event")):
    self.endTime = pygame.time.get_ticks() + (wait * 1000)
    self.wait = wait
    self.trigger = trigger

  def updateEvent(self):
      currentTime = pygame.time.get_ticks()
      if currentTime >= self.endTime:
        self.trigger()
        self.endTime = currentTime + (self.wait * 1000)


class SplashScreen:
  def __init__(self, screen, wait = 3):
    self.screen = screen
    image_path = resource_path("resources/jamSmall.png")
    self.org_icon_image = pygame.image.load(image_path)
    image_width, image_height = self.org_icon_image.get_size()
    self.aspect = image_height / image_width
    self.y = 0
    self.endTime = pygame.time.get_ticks() + (wait * 1000)
    self.wait = wait
    self.splash = pygame.transform.scale(self.org_icon_image, self.getSplashSize())
    self.shouldRender = True

  def getSplashSize(self):
    screen_rect = self.screen.get_rect()
    sacled_height = int(screen_rect.width * self.aspect)
    self.y = (screen_rect.height - sacled_height) // 2
    return (screen_rect.width, sacled_height)

  def render(self):
    self.screen.fill((0, 0, 0))
    self.screen.blit(self.splash, (0,self.y))

  def shouldDisplaySplash(self):
    if self.shouldRender:
      currentTime = pygame.time.get_ticks()
      if currentTime >= self.endTime:
        self.shouldRender = False
    return self.shouldRender
  
  def update(self):
    self.splash = pygame.transform.scale(self.org_icon_image, self.getSplashSize())

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
