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
    self.playableArea = ((10,50), (self.width - 20, self.height - 130))
    self.clickable = True

  def setup(self):
    # Settup bottom row buttons
    (pos, size) = self.calcBottomButtonPosNSize(4, 20, 20, 10)
    colors = ((220,220,220),(180,140,140))
    self.buttons.append(TextButton(pos[0], "Profile", size[0], colors, (255,0,0), (True, True)))
    self.buttons.append(TextButton(pos[1], "Quacker", size[1], colors, (255,0,0), (True, True)))
    self.buttons.append(TextButton(pos[2], "News", size[2], colors, (255,0,0), (True, True)))
    self.buttons.append(TextButton(pos[3], "Store", size[3], colors, (255,0,0), (True, True)))

  def render(self, events):
    screen = self.screen
    # Ignore events if we cant be clicked
    availableEvents = events if self.clickable else []
    # render playable area
    pygame.draw.rect(screen, (255,255,255), self.playableArea)
    # render bottom row buttons
    for button in self.buttons:
      button.render(screen, availableEvents)

  def update(self):
    rect = self.screen.get_rect()
    self.width = rect.width
    self.height = rect.height
    # update playable area scale and pos
    self.playableArea = ((10,50), (self.width - 20, self.height - 130))
    # update bottom row buttons scale and pos
    (pos, size) = self.calcBottomButtonPosNSize(len(self.buttons), 20, 20, 10)
    for index, button in enumerate(self.buttons):
      button.update(pos[index], size[index])

  def calcBottomButtonPosNSize(self, numOButtons, offsetx, offesty, padding):
    # Calculate the positions of buttons
    pos = []
    size = []
    cx = offsetx
    wid = ((self.width - ((offsetx * 2) + ((numOButtons - 1) * padding))) // numOButtons)
    for i in range(0, numOButtons):
      pos.append((cx, self.height - (offesty + self.sizeY)))
      size.append((wid, self.sizeY))
      cx += (wid + padding)
    return (pos, size)
  
  def setClickable(self, isClickable = None):
    clickable = isClickable
    if clickable == None:
      clickable = not self.clickable
    self.clickable = clickable