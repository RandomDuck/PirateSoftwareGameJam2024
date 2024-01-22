import pygame
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
  def __init__(self, screen, size, color, text_color, toggleCB = lambda:""):
    self.toggleCB = toggleCB
    self.screen = screen
    self.color = color
    self.text_color = text_color
    rect = screen.get_rect()
    self.window_width = rect.width
    self.window_height = rect.height
    self.size = size
    self.pos = (self.window_width - (self.size[0]+10), 10)
    self.CoverRect = pygame.Rect(self.pos[0]-5, self.pos[1]-5, size[0]+10, size[1]+10)  
    self.active = False
    self.button = None
    self.options = {}
    
  def getAspectPos(self):
    return (self.pos[0]+5,self.size[1]+20), (self.size[0]-10, self.size[1])

  def setup(self):
    self.button = btn(self.pos, "Settings", self.size, self.color, self.text_color, (True, True), self.toggle)
    aspectPos = self.getAspectPos()
    self.options["aspect"] = AspectButton(self.screen, aspectPos[0], aspectPos[1], self.color, self.text_color)
    self.CoverRect.height = (self.size[1] + 10) * (len(self.options) + 1)
  
  def render(self, events):
    if self.active:
      pygame.draw.rect(self.screen, (100,0,100), self.CoverRect)
    self.button.render(self.screen, events)
    if self.active:
      for option in self.options:
        self.options[option].render(events)

  def toggle(self):
    self.toggleCB()
    self.active = not self.active
    self.button.toggle()

  def getAspect(self):
    return self.options["aspect"].getRatio()
  
  def update(self):
    rect = self.screen.get_rect()
    self.window_width = rect.width
    self.window_height = rect.height
    self.pos = (self.window_width - (self.size[0]+10), 10)
    self.CoverRect.x = self.pos[0]-5
    self.CoverRect.y = self.pos[1]-5
    self.button.update(self.pos, self.size)
    aspectPos = self.getAspectPos()
    self.options["aspect"].update(aspectPos[0], aspectPos[1])