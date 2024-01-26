from ..components.page import Page
from ..components.text import TextBox
from ..components.button import TextButton

class News(Page):
  def __init__(self, screen, area, gameCon):
    super().__init__(screen, area, gameCon)
    self.setup()

  def setup(self):
    self.banner = TextBox(self.pos,self.size,"News",(255,255,255),(0,0,255),(True,True))
    self.ads = TextButton(self.pos,"Post ads (+100 followers, -2000 cash)",self.size,((100,100,100),(0,0,255)),(255,255,255),(True,True), lambda:self.purchase(-2000,100))
    self.follows = TextButton(self.pos,"Sell gossip (+800 cash, -80 followers)",self.size,((100,100,100),(0,0,255)),(255,255,255),(True,True), lambda:self.purchase(800,-80))
    self.elements.append(self.banner)
    self.buttons.append(self.follows)
    self.buttons.append(self.ads)

  def purchase(self, cash, follows):
    currentCash = self.gameCon.getCash()
    currentFollows = self.gameCon.getFollowers()
    if cash < 0:
      #we are bying using cash
      if currentCash - -cash >= 0:
        self.gameCon.updateCash(cash)
        self.gameCon.updateFollowers(follows)
    else:
      if currentFollows - -follows >= 0:
        self.gameCon.updateCash(cash)
        self.gameCon.updateFollowers(follows)

  
  def update(self, area):
    super().update(area)
    self.banner.update(self.pos, (self.size[0],30))
    self.follows.update((self.pos[0]+5, self.pos[1]+40), (self.size[0]-10,60))
    self.ads.update((self.pos[0]+5, self.pos[1]+110), (self.size[0]-10,60))