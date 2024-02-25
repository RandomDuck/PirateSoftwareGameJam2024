import pygame

class Text: #renders text on screen
  def __init__(self, position, size, text, color, center, texsize = 36):
    self.font = pygame.font.Font(None, texsize)
    self.text = text
    self.size = size
    self.text_color = color
    self.pos = position
    self.center = center

  def render(self, surface):
    text_surface = self.font.render(self.text, True, self.text_color)
    text_rect = text_surface.get_rect()
    if self.center[0]:
      if self.center[1]:
        text_rect.center = ((self.size[0] // 2) + self.pos[0], (self.size[1] // 2) + self.pos[1])
      else:
        text_rect.centery = (self.size[1] // 2) + self.pos[1]
        text_rect.left = self.pos[0] + 5
    elif self.center[1]:
      text_rect.centerx = (self.size[0] // 2) + self.pos[0]
      text_rect.top = self.pos[1]
    else:
      text_rect.topleft = self.pos
    surface.blit(text_surface, text_rect)

  def update(self, pos, size):
    self.size = size
    self.pos = pos

class TextBox(Text): #renders text on screen with a background
  def __init__(self, position, size, text, color, backgroundColor, center, texsize = 36):
    super().__init__(position, size, text, color, center, texsize)
    self.background_rect = pygame.Rect(position[0], position[1], size[0], size[1])  
    self.background_color  = backgroundColor 
  
  def render (self, surface):
    pygame.draw.rect(surface, self.background_color, self.background_rect)
    super().render(surface)

  def update(self, pos, size):
    self.background_rect = pygame.Rect(pos[0], pos[1], size[0], size[1])  
    super().update(pos, size)
