import pygame

class Text: #renders text on screen
  def __init__(self, position, text, color, center):
    self.font = pygame.font.Font(None, 36)
    self.text = text
    self.text_color = color
    self.pos = position
    self.center = center

  def render(self, surface):
    text_surface = self.font.render(self.text, True, self.text_color)
    text_rect = text_surface.get_rect()
    if self.center:
      text_rect.center = (self.pos[0] // 2, self.pos[1] // 2)
    else:
      text_rect.center = self.pos
    surface.blit(text_surface, text_rect)

class TextBox(Text): #renders text on screen with a background
  def __init__(self, position, size, text, color, backgroundColor, center):
    super().__init__(position, text, color, center)
    self.background_rect = pygame.Rect(position[0], position[1], size[0], size[1])  
    self.background_color  = backgroundColor 
  
  def render (self, surface):
    pygame.draw.rect(surface, self.background_color, self.background_rect)
    super().render(surface)
