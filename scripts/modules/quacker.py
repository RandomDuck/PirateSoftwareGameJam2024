from ..components.page import Page
from ..components.text import TextBox
from ..components.button import TextButton

class Quacker(Page):
  def __init__(self, screen, area, gameCon):
    super().__init__(screen, area, gameCon)
    self.setup()

  def setup(self):
    self.banner = TextBox(self.pos,(self.size[0],30),"Quacker",(255,255,255),(255,0,0),(True,True))
    self.post = TextButton((self.pos[0]+10, self.pos[1]+40),"Make post (+10 followers)",(self.size[0]-20,60),((255,255,0),(255,0,0)),(100,100,100),(True,True), lambda:self.gameCon.updateFollowers(10))
    self.post = TextButton((self.pos[0]+10, self.pos[1]+40),"Post fake news (-10 follows, +20 cash)",(self.size[0]-20,60),((255,255,0),(255,0,0)),(100,100,100),(True,True), lambda:self.sellFollows())
    self.elements.append(self.banner)
    self.buttons.append(self.post)

  def sellFollows(self):
    if self.gameCon.getFollowers() >= 10:
      self.gameCon.updateFollowers(-10)
      self.gameCon.updateCash(20)
  
  def update(self, area):
    super().update(area)
    self.banner.update(self.pos, (self.size[0],30))
    self.post.update((self.pos[0]+10, self.pos[1]+40),(self.size[0]-20,60))