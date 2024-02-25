import pygame

class Icon:
  def __init__(self, image_path, position, size):
    self.original_image = pygame.image.load(image_path)
    self.size = size
    self.position = position
    self.image = pygame.transform.scale(self.original_image, size)

  def render(self, surface):
    surface.blit(self.image, self.position)

  def update(self, position, size):
    self.size = size
    self.position = position
    self.image = pygame.transform.scale(self.original_image, size)

class IconBox(Icon):
  def __init__(self, image_path, position, size, backgroundColor, padding = 15):
    self.padding = padding
    spadding = self.padding*2
    iconP = (position[0] + padding, position[1] + padding)
    iconS = (size[0] - spadding, size[1] - spadding)
    super().__init__(image_path, iconP, iconS)
    self.background_rect = pygame.Rect(position[0], position[1], size[0], size[1])  
    self.background_color  = backgroundColor 
  
  def render (self, surface):
    pygame.draw.rect(surface, self.background_color, self.background_rect)
    super().render(surface)

  def update(self, pos, size):
    self.size = size
    self.position = pos
    spadding = self.padding*2
    iconP = (pos[0] + self.padding, pos[1] + self.padding)
    iconS = (size[0] - spadding, size[1] - spadding)
    self.background_rect = pygame.Rect(pos[0], pos[1], size[0], size[1])  
    super().update(iconP, iconS)