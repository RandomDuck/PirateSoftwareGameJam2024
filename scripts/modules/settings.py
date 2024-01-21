from ..components.button import TextButton as btn

class AspectButton:
  def __init__(self, screen, pos, size, color, text_color):
    self.screen = screen
    self.color = color
    self.text_color = text_color
    self.size = size
    self.ratio_text = ["S","M","L"]
    self.ratios = [(560,840), (720,1080), (800,1200)]
    self.select_ratio = 0
    self.defaultText = "Screensize:"
    self.button = btn(pos, f'{self.defaultText} {self.ratio_text[self.select_ratio]}', self.size, self.color, self.text_color, (True, True), self.toggleRatio)

  def render(self, events):
    self.button.render(self.screen, events)

  def toggleRatio(self):
    self.select_ratio += 1
    if self.select_ratio >= len(self.ratios):
      self.select_ratio = 0
    self.button.changeText(f'{self.defaultText} {self.ratio_text[self.select_ratio]}')

  def getRatio(self):
    return self.ratios[self.select_ratio]
  
  def update(self, pos, size):
    self.button.update(pos, size)
  
class Settings:
  def __init__(self, screen, size, color, text_color):
    self.screen = screen
    self.color = color
    self.text_color = text_color
    rect = screen.get_rect()
    self.window_width = rect.width
    self.window_height = rect.height
    self.size = size
    self.pos = (self.window_width - (self.size[0]+10), 10)
    self.active = False
    self.button = None
    self.options = {}

  def setup(self):
    self.button = btn(self.pos, "Settings", self.size, self.color, self.text_color, (True, True), self.toggle)
    self.options["aspect"] = AspectButton(self.screen, (self.pos[0],self.size[1]+20), self.size, self.color, self.text_color)
  
  def render(self, events):
    self.button.render(self.screen, events)
    if self.active:
      for option in self.options:
        self.options[option].render(events)

  def toggle(self):
    self.active = not self.active
    self.button.toggle()

  def getAspect(self):
    return self.options["aspect"].getRatio()
  
  def update(self):
    rect = self.screen.get_rect()
    self.window_width = rect.width
    self.window_height = rect.height
    self.pos = (self.window_width - (self.size[0]+10), 10)
    self.button.update(self.pos, self.size)
    self.options["aspect"].update((self.pos[0],self.size[1]+20), self.size)