import pygame
import text as txt

class Buttion: # Renders a button with text
  def __init__(self, position, size, color):
    self.color = color
    self.pos = position
    self.size = size
    self.button_rect = pygame.Rect(position[0], position[1], size[0], size[1])  
    self.button_color  = color

  def render(self, surface):
    pygame.draw.rect(surface, self.button_color, self.button_rect)

class TextButtion: # Renders a button with text
  def __init__(self, position, text, size, color, text_color):
    self.color = color
    self.pos = position
    self.size = size
    self.button_rect = pygame.Rect(position[0], position[1], size[0], size[1])  
    self.button_color  = color
    self.text_obj = txt.Text(position, text, text_color, True)

  def render(self, surface):
    pygame.draw.rect(surface, self.button_color, self.button_rect)
    self.text_obj.render(surface)


class IconButtion: # Renders a button with an icon
  def __init__(self, iconPath, position, size, color):
    icon = pygame.image.load(iconPath)
    self.icon = pygame.transform.scale(icon, (50, 50))
    self.color = color
    self.pos = position
    self.size = size
    self.button_rect = pygame.Rect(position[0], position[1], size[0], size[1])  
    self.button_color  = color  

  def render(self, surface):
    pygame.draw.rect(surface, self.button_color, self.button_rect)
    surface.blit(self.icon, (self.button_rect.x, self.button_rect.y,))
