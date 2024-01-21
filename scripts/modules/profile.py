# TODO: fix profile layout and functionality
class ProfilePage:
  def __init__(self, screen):
    self.screen = screen
    rect = screen.get_rect()
    self.width = rect.width
    self.height = rect.height
    self.elements = []

  def setup(self):
    pass

  def render(self, events):
    screen = self.screen
    for element in self.elements:
      element.render(screen, events)