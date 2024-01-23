import pygame
from ..components.button import TextButton as btn

class settingsButton:
  def __init__(self, screen, pos, size, color, text_color, callback, text):
    self.screen = screen
    self.color = color
    self.text_color = text_color
    self.size = size
    self.button = btn(pos, text, self.size, self.color, self.text_color, (True, True), callback)
  
  def render(self, events):
    self.button.render(self.screen, events)

  def update(self, pos, size):
    self.button.update(pos, size)

class AspectButton(settingsButton):
  def __init__(self, screen, pos, size, color, text_color):
    self.ratio_text = ["S","M","L"]
    self.ratios = [(560,840), (720,1080), (800,1200)]
    self.select_ratio = 0
    self.defaultText = "Screensize:"
    super().__init__(screen, pos, size, color, text_color, self.toggleRatio, f'{self.defaultText} {self.ratio_text[self.select_ratio]}')

  def toggleRatio(self):
    self.select_ratio += 1
    if self.select_ratio >= len(self.ratios):
      self.select_ratio = 0
    self.button.changeText(f'{self.defaultText} {self.ratio_text[self.select_ratio]}')

  def getRatio(self):
    return self.ratios[self.select_ratio]
  
class SaveButton(settingsButton):
  def __init__(self, screen, pos, size, color, text_color):
    super().__init__(screen, pos, size, color, text_color, self.SaveGame, 'Save')

  def SaveGame(self):
    pass # TODO: add way to save game

class ResetButton(settingsButton):
  def __init__(self, screen, pos, size, color, text_color):
    super().__init__(screen, pos, size, color, text_color, self.ResetGame, 'Reset')

  def ResetGame(self):
    pass # TODO: add way to reset game

class QuitButton(settingsButton):
  def __init__(self, screen, pos, size, color, text_color):
    super().__init__(screen, pos, size, color, text_color, self.Quit, 'Quit')

  def Quit(self):
    # TODO: Save game on quit
    pygame.event.post(pygame.event.Event(pygame.QUIT))
  
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
    
  def getButtonsPos(self):
    pos = []
    lasty = (self.size[1]+20)
    for i in range(0, 4):
      pos.append(((self.pos[0]+5),lasty))
      lasty += (self.size[1]+10)
    return (pos, (self.size[0]-10, self.size[1]))

  def setup(self):
    self.button = btn(self.pos, "Settings", self.size, self.color, self.text_color, (True, True), self.toggle)
    (pos, size) = self.getButtonsPos()
    self.options["aspect"] = AspectButton(self.screen, pos[0], size, self.color, self.text_color)
    self.options["save"] = SaveButton(self.screen, pos[1], size, self.color, self.text_color)
    self.options["reset"] = ResetButton(self.screen, pos[1], size, self.color, self.text_color)
    self.options["quit"] = QuitButton(self.screen, pos[2], size, self.color, self.text_color)
    self.CoverRect.height = (self.size[1] + 10) * (len(self.options) + 1)
  
  def render(self, events):
    if self.active:
      pygame.draw.rect(self.screen, (100,0,100), self.CoverRect)
      for option in self.options:
        self.options[option].render(events)
    self.button.render(self.screen, events)

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
    (pos, size) = self.getButtonsPos()
    self.options["aspect"].update(pos[0], size)
    self.options["save"].update(pos[1], size)
    self.options["reset"].update(pos[2], size)
    self.options["quit"].update(pos[3], size)