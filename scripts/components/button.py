import pygame
from .text import Text

class Button: # Renders a button with text
  def __init__(self, position, size, color, callback = lambda:print("clicked button")):
    self.pos = position #Expected data config: (x,y)
    self.size = size #Expected data config: (x,y)
    self.button_rect = pygame.Rect(position[0], position[1], size[0], size[1])  
    self.button_color  = color #Expected data config: ((r,g,b),(r,g,b))
    self.callback = callback #Expected data config: function or null
    self.pressed = False

  def render(self, surface, events):
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseIsHovering = (mouseX >= self.pos[0] and mouseX <= (self.pos[0] + self.size[0])) and (mouseY >= self.pos[1] and mouseY <= (self.pos[1] + self.size[1]))
    pygame.draw.rect(surface, self.button_color[1] if mouseIsHovering else self.button_color[0], self.button_rect)
    if pygame.MOUSEBUTTONUP in events and mouseIsHovering:
      self.callback()


class TextButton(Button): # Renders a button with text
  def __init__(self, position, text, size, color, text_color, center, callback = lambda:print("clicked text button")):
    super().__init__(position, size, color, callback)
    self.text_obj = Text(position, size, text, text_color, center)

  def render(self, surface, events):
    super().render(surface, events)
    self.text_obj.render(surface)


class IconButton(Button): # Renders a button with an icon
  def __init__(self, iconPath, position, size, color, callback = lambda:print("clicked icon button")):
    super().__init__(position, size, color, callback)
    icon = pygame.image.load(iconPath)
    self.icon = pygame.transform.scale(icon, (50, 50))

  def render(self, surface, events):
    super().render(surface, events)
    surface.blit(self.icon, (self.button_rect.x, self.button_rect.y,))
