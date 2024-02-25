from ..components.page import Page
from ..components.text import TextBox
from ..components.store_Item import StoreItem
from resources.datasets.storeItems import storeItems

class Store(Page):#TODO: make cred into followers
  def __init__(self, screen, area, gameCon):
    super().__init__(screen, area, gameCon)
    self.setup()

  def setup(self):
    self.banner = TextBox(self.pos,self.size,"Store",(255,255,255),(0,0,0),(True,True))
    posy=35
    for index, item in enumerate(storeItems):
      self.buttons.append(StoreItem((self.pos[0], self.pos[1]+(posy * index)), self.size, item, self.gameCon))
    self.elements.append(self.banner)
  
  def update(self, area):
    super().update(area)
    self.banner.update(self.pos, (self.size[0],30))

    posy=35
    for button in self.buttons:
      button.update((self.pos[0]+5, self.pos[1]+posy), (self.size[0]-10, 60))
      posy += 65