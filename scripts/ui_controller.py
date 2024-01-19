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
    self.buttons.append(TextButton((20,self.height - 70), "Profile", ((self.width / 3)-20,50), ((255,255,255),(255,127,127)), (255,0,0), (True, True)))
    self.buttons.append(TextButton(((self.width/3) + 10,self.height - 70), "Quacker", ((self.width / 3)-20,50), ((255,255,255),(255,127,127)), (255,0,0), (True, True)))
    self.buttons.append(TextButton(((self.width/3) * 2,self.height - 70), "Store", ((self.width / 3)-20,50), ((255,255,255),(255,127,127)), (255,0,0), (True, True)))

  def render(self, events):
    screen = self.screen
    for button in self.buttons:
      button.render(screen, events)