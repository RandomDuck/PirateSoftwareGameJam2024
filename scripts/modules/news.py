from ..components.page import Page
from ..components.text import TextBox

class News(Page):
  def __init__(self, screen, area):
    super().__init__(screen, area)
    self.setup()
  def setup(self):
    self.elements.append(TextBox(self.pos,self.size,"news",(255,255,255),(0,0,255),(True,True)))