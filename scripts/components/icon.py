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