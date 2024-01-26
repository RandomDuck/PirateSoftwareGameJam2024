from ..components.page import Page
from ..components.text import TextBox, Text

class ProfilePage(Page):
  def __init__(self, screen, area, gameCon):
    super().__init__(screen, area, gameCon)
    self.setup()
    
  def setup(self):
    self.banner = TextBox(self.pos,(self.size[0],30),"Profile",(255,255,255),(0,200,0),(True,True))
    self.user = TextBox((self.pos[0]+10, self.pos[1]+40), (self.size[0]-20,50),"Tharr plunderer of scripts",(255,255,255),(0,100,0),(True,True))
    self.cash = Text((self.pos[0]+10, self.pos[1]+100), (self.size[0]-20,30),f"Cash: {self.gameCon.getCash()}",(0,100,0),(True,True))
    self.follows = Text((self.pos[0]+10, self.pos[1]+130), (self.size[0]-20,30),f"Follows: {self.gameCon.getFollowers()}",(0,100,0),(True,True))
    self.fps = Text((self.pos[0]+10, self.pos[1]+160), (self.size[0]-20,30),f"Followers per second: {self.gameCon.getfollowersPerSecond()}",(0,100,0),(True,True))
    self.elements.append(self.banner)
    self.elements.append(self.user)
    self.elements.append(self.follows)
    self.elements.append(self.cash)
    self.elements.append(self.fps)

  def render(self, events):
    super().render(events)
    self.cash.text = f"Cash: {self.gameCon.getCash()}"
    self.follows.text = f"Follows: {self.gameCon.getFollowers()}"
    self.fps.text = f"Followers per second: {self.gameCon.getfollowersPerSecond()}"
  
  def update(self, area):
    super().update(area)
    self.banner.update(self.pos, (self.size[0],30))
    self.user.update((self.pos[0]+10, self.pos[1]+40), (self.size[0]-20,50))
    self.cash.update((self.pos[0]+10, self.pos[1]+100), (self.size[0]-20,30))
    self.follows.update((self.pos[0]+10, self.pos[1]+130), (self.size[0]-20,30))
    self.fps.update((self.pos[0]+10, self.pos[1]+160), (self.size[0]-20,30))
    #sizeCalc = self.size[1]-190