class Page:
  def __init__(self, screen, area):
    self.screen = screen
    self.pos = area[0]
    self.size = area[1]
    self.elements = []
    self.buttons = []

  def render(self, events):
    screen = self.screen
    for element in self.elements:
      element.render(screen)
    for button in self.buttons:
      button.render(screen, events)

  def update(self, area):
    self.pos = area[0]
    self.size = area[1]
    for element in self.elements:
      element.update(area[0], area[1])