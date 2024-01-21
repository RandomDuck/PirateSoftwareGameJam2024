from .components.button import TextButton
import pygame

class UiController:
  def __init__(self, screen):
    self.screen = screen
    rect = screen.get_rect()
    self.width = rect.width
    self.height = rect.height
    self.sizeY = 50 
    self.buttons = []

  def setup(self):
    (pos, size) = self.calcBottomButtonPosNSize(4, 20, 20, 10)
    self.buttons.append(TextButton(pos[0], "Profile", size[0], ((255,255,255),(255,127,127)), (255,0,0), (True, True)))
    self.buttons.append(TextButton(pos[1], "Quacker", size[1], ((255,255,255),(255,127,127)), (255,0,0), (True, True)))
    self.buttons.append(TextButton(pos[2], "News", size[2], ((255,255,255),(255,127,127)), (255,0,0), (True, True)))
    self.buttons.append(TextButton(pos[3], "Store", size[3], ((255,255,255),(255,127,127)), (255,0,0), (True, True)))

  def render(self, events):
    screen = self.screen
    for button in self.buttons:
      button.render(screen, events)

  def update(self):
    rect = self.screen.get_rect()
    self.width = rect.width
    self.height = rect.height
    (pos, size) = self.calcBottomButtonPosNSize(len(self.buttons), 20, 20, 10)
    for index, button in enumerate(self.buttons):
      button.update(pos[index], size[index])

  def calcBottomButtonPosNSize(self, numOButtons, offsetx, offesty, padding):
    pos = []
    size = []
    cx = offsetx
    wid = ((self.width - ((offsetx * 2) + ((numOButtons - 1) * padding))) // numOButtons)
    for i in range(0, numOButtons):
      pos.append((cx, self.height - (offesty + self.sizeY)))
      size.append((wid, self.sizeY))
      cx += (wid + padding)
    return (pos, size)