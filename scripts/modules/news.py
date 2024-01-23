from ..components.page import Page
from ..components.text import TextBox

class News(Page):
  def __init__(self, screen, area, gameCon):
    super().__init__(screen, area, gameCon)
    self.setup()
  def setup(self):
    self.banner = TextBox(self.pos,self.size,"News",(255,255,255),(0,0,255),(True,True))
    self.elements.append(self.banner)
  
  def update(self, area):
    super().update(area)
    self.banner.update(self.pos, (self.size[0],30))