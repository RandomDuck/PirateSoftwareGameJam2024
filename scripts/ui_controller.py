from .components.button import TextButton
import pygame

class UiController:
  def __init__(self, screen):
    self.screen = screen
    rect = screen.get_rect()
    self.width = rect.width
    self.height = rect.height
    self.buttons = []

  def setup(self):
    self.buttons.append(TextButton((20,20), "Hello world", (self.width-40,50), ((255,255,255),(255,127,127)), (255,0,0), (True, True)))

  def render(self, events):
    screen = self.screen
    for button in self.buttons:
      button.render(screen, events)