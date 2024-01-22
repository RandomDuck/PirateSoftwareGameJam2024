import pygame

def setGameIcon():
  # Set game icon
  image_path = "resources/icon.jpg"
  image_width, image_height = (128,128)
  icon_image = pygame.image.load(image_path)
  icon_image = pygame.transform.scale(icon_image, (image_width,image_height))

  # Create a surface with per-pixel alpha
  image_surface = pygame.Surface((image_width, image_height), pygame.SRCALPHA)

  # Draw the image onto the alpha surface
  image_surface.blit(icon_image, (0, 0))

  # Create a circular mask
  mask_radius = min(image_width, image_height) // 2
  mask = pygame.Surface((mask_radius * 2, mask_radius * 2), pygame.SRCALPHA)
  pygame.draw.circle(mask, (255, 255, 255, 255), (mask_radius, mask_radius), mask_radius)

  # Apply the circular mask to the image surface
  image_surface.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
  pygame.display.set_icon(image_surface)

def setGameName():
  pass

# Event handleing
def fetchEvents():
  events = []
  for event in pygame.event.get():
      events.append(event.type)
  return events
