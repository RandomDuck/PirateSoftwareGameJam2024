class Page:
  def __init__(self, screen):
    self.screen = screen
    rect = screen.get_rect()
    self.width = rect.width
    self.height = rect.height
    self.elements = []

  def render(self, events):
    screen = self.screen
    for element in self.elements:
      element.render(screen, events)