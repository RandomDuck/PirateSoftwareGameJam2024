import pygame
from .text import Text
from .icon import Icon

class Button: # Renders a button with text
  def __init__(self, position, size, color, callback = lambda:print("clicked button"), toggleNclickColors=((0,0,0), (0,200,200))):
    self.pos = position #Expected data config: (x,y)
    self.size = size #Expected data config: (x,y)
    self.button_rect = pygame.Rect(position[0], position[1], size[0], size[1])  
    self.button_color  = color #Expected data config: ((r,g,b),(r,g,b))
    self.toggleNclickColors = toggleNclickColors
    self.clickColor = toggleNclickColors[0]
    self.clickAlpha = (self.clickColor[0], self.clickColor[1], self.clickColor[2], 128)
    self.overlay = pygame.Surface(self.size, pygame.SRCALPHA)
    self.overlay.fill(self.clickAlpha)
    self.callback = callback #Expected data config: function or null
    self.toggled = False
    self.downOnHover = False

  def render(self, surface, events):
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseIsHovering = (mouseX >= self.pos[0] and mouseX <= (self.pos[0] + self.size[0])) and (mouseY >= self.pos[1] and mouseY <= (self.pos[1] + self.size[1]))
    
    # dont change color on hover if disabled
    if type(events) != type([]):
      mouseIsHovering = False
      events = []

    # Set button colors
    standardButtonColor = self.button_color[1] if mouseIsHovering else self.button_color[0]
    toggledButtonColors = self.button_color[1] if mouseIsHovering else self.toggleNclickColors[1]
    buttonColor = standardButtonColor if not self.toggled else toggledButtonColors
    showClick = False

    # Handle button press
    if pygame.MOUSEBUTTONUP in events:
      if mouseIsHovering and self.downOnHover:
        self.callback()
      if self.downOnHover:
        self.downOnHover = False
    
    if pygame.MOUSEBUTTONDOWN in events and mouseIsHovering:
      showClick = True
      self.downOnHover = True
    
    if self.downOnHover and mouseIsHovering:
      showClick = True

    # draw button
    pygame.draw.rect(surface, buttonColor, self.button_rect)
    if showClick:
      surface.blit(self.overlay, self.pos)

  def toggle(self):
    self.toggled = not self.toggled

  def update(self, pos, size):
    self.pos = pos
    self.size = size
    self.overlay = pygame.Surface(self.size, pygame.SRCALPHA)
    self.overlay.fill(self.clickAlpha)
    self.button_rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

class TextButton(Button): # Renders a button with text
  def __init__(self, position, text, size, color, text_color, center, callback = lambda:print("clicked text button"), toggleNclickColors=((0,0,0), (0,200,200))):
    super().__init__(position, size, color, callback, toggleNclickColors)
    self.text_obj = Text(position, size, text, text_color, center)

  def render(self, surface, events):
    super().render(surface, events)
    self.text_obj.render(surface)

  def changeText(self, newText):
    self.text_obj.text = newText

  def update(self, pos, size):
    super().update(pos, size)
    self.text_obj.update(pos, size)

class IconButton(Button): # Renders a button with an icon
  def __init__(self, iconPath, position, size, color, padding = 15, callback = lambda:print("clicked icon button"), toggleNclickColors=((0,0,0), (0,200,200))):
    super().__init__(position, size, color, callback, toggleNclickColors)
    self.padding = padding
    spadding = self.padding*2
    iconP = (position[0] + padding, position[1] + padding)
    iconS = (size[0] - spadding, size[1] - spadding)
    self.icon = Icon(iconPath, iconP, iconS)

  def render(self, surface, events):
    super().render(self, surface, events)
    self.icon.render(surface)

  def update(self, pos, size):
    super().update(pos, size)
    spadding = self.padding*2
    iconP = (pos[0] + self.padding, pos[1] + self.padding)
    iconS = (size[0] - spadding, size[1] - spadding)
    self.icon.update(iconP, iconS)
