from ..components.page import Page
from ..components.text import TextBox
from ..components.button import TextButton

class News(Page):
  def __init__(self, screen, area, gameCon):
    super().__init__(screen, area, gameCon)
    self.setup()

  def setup(self):
    self.banner = TextBox(self.pos,self.size,"News",(255,255,255),(0,0,255),(True,True))
    self.ads = TextBox(self.pos,self.size,"Post ads (+100 followers, -10000 cash)",(255,255,255),(0,0,255),(True,True))
    self.follows = TextBox(self.pos,self.size,"Sell follower gossip (+800 cash, -80 followers)",(255,255,255),(0,0,255),(True,True))
    self.elements.append(self.banner)
    self.buttons.append(self.follows)
    self.buttons.append(self.ads)
  
  def update(self, area):
    super().update(area)
    self.banner.update(self.pos, (self.size[0],30))
    self.follows.update((self.pos[0]+5, self.pos[1]+40), (self.size[0]-10,30))
    self.ads.update((self.pos[0]+5, self.pos[1]+80), (self.size[0]-10,30))