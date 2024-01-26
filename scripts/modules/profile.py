from ..components.page import Page
from ..components.text import TextBox, Text
from ..components.icon import IconBox

class ProfilePage(Page):
  def __init__(self, screen, area, gameCon):
    super().__init__(screen, area, gameCon)
    self.setup()
    
  def setup(self):
    self.banner = TextBox(self.pos,(self.size[0],30),"Profile",(255,255,255),(0,200,0),(True,True))
    self.user = TextBox((self.pos[0]+10, self.pos[1]+45), (self.size[0]-20,40),"Tharr plunderer of scripts",(255,255,255),(0,100,0),(True,True))
    self.cash = Text((self.pos[0]+120, self.pos[1]+100), (self.size[0]-130,30),f"Cash: {self.gameCon.getCash()}",(0,100,0),(True,False))
    self.follows = Text((self.pos[0]+120, self.pos[1]+130), (self.size[0]-130,30),f"Follows: {self.gameCon.getFollowers()}",(0,100,0),(True,False))
    self.fps = Text((self.pos[0]+120, self.pos[1]+160), (self.size[0]-130,30),f"Followers per second: {self.gameCon.getfollowersPerSecond()}",(0,100,0),(True,False))
    self.icon = IconBox("resources/profile.png",(self.pos[0]+10, self.pos[1]+95), (100,100), (0,125,125), 5)
    self.elements.append(self.banner)
    self.elements.append(self.user)
    self.elements.append(self.follows)
    self.elements.append(self.cash)
    self.elements.append(self.fps)
    self.elements.append(self.icon)

  def render(self, events):
    super().render(events)
    self.cash.text = f"Cash: {self.gameCon.getCash()}"
    self.follows.text = f"Follows: {self.gameCon.getFollowers()}"
    self.fps.text = f"Followers per second: {self.gameCon.getfollowersPerSecond()}"
  
  def update(self, area):
    super().update(area)
    self.banner.update(self.pos, (self.size[0],30))
    self.user.update((self.pos[0]+10, self.pos[1]+45), (self.size[0]-20,40))
    self.cash.update((self.pos[0]+120, self.pos[1]+100), (self.size[0]-130,30))
    self.follows.update((self.pos[0]+120, self.pos[1]+130), (self.size[0]-130,30))
    self.fps.update((self.pos[0]+120, self.pos[1]+160), (self.size[0]-130,30))
    self.icon.update((self.pos[0]+10, self.pos[1]+95), (100,100))
    #sizeCalc = self.size[1]-190