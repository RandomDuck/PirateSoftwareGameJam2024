import pygame
from .text import Text
from .icon import Icon

class Button: # Renders a button with text
  def __init__(self, position, size, color, callback = lambda:print("clicked button")):
    self.pos = position #Expected data config: (x,y)
    self.size = size #Expected data config: (x,y)
    self.button_rect = pygame.Rect(position[0], position[1], size[0], size[1])  
    self.button_color  = color #Expected data config: ((r,g,b),(r,g,b))
    self.callback = callback #Expected data config: function or null
    self.toggled = False
    self.downOnHover = False

  def render(self, surface, events):
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseIsHovering = (mouseX >= self.pos[0] and mouseX <= (self.pos[0] + self.size[0])) and (mouseY >= self.pos[1] and mouseY <= (self.pos[1] + self.size[1]))
    pygame.draw.rect(surface, self.button_color[1] if mouseIsHovering else self.button_color[0], self.button_rect)
    
    if pygame.MOUSEBUTTONUP in events:
      if mouseIsHovering and self.downOnHover:
        self.callback()
      if self.downOnHover:
        self.downOnHover = False
    
    if pygame.MOUSEBUTTONDOWN in events and mouseIsHovering:
      self.downOnHover = True

  def toggle(self):
    self.button_color = (self.button_color[1], self.button_color[0])
    self.toggled = not self.toggled

  def update(self, pos, size):
    self.pos = pos
    self.size = size
    self.button_rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

class TextButton(Button): # Renders a button with text
  def __init__(self, position, text, size, color, text_color, center, callback = lambda:print("clicked text button")):
    super().__init__(position, size, color, callback)
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
  def __init__(self, iconPath, position, size, color, padding = 15, callback = lambda:print("clicked icon button")):
    super().__init__(position, size, color, callback)
    spadding = padding*2
    self.icon = Icon(iconPath, (position[0] + padding, position[1] + padding), (size[0] - spadding, size[1] - spadding))

  def render(self, surface, events):
    super().render(surface, events)
    self.icon.render(surface)

  def update(self, pos, size):
    super().update(pos, size)
    self.icon.update(pos, size)
