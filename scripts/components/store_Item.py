from .button import Button
from .text import Text
from .icon import Icon

class StoreItem:
  def __init__(self, pos, size, storeItem, gameCon):
    self.pos = pos
    self.size = size
    self.itemData = storeItem
    self.gameCon = gameCon
    self.button = Button(pos, size, ((100,100,100), (120,120,120)), self.purchase)
    self.title = Text(pos,size, self.itemData["title"], (255,255,255), (True,True))
    self.description = Text(pos,size, self.itemData["description"], (255,255,255), (True,True), 22)
    self.icon = Icon(self.itemData["iconPath"], pos, size)
    self.setup()

  def calculateItemPositionsAndSize(self):
    data = {
      "title": {
        "pos": (self.pos[0]+65, self.pos[1]+10),
        "size": (self.size[0]-85,20)
      },
      "description": {
        "pos": (self.pos[0]+65, self.pos[1]+35),
        "size": (self.size[0]-85,20)
      },
      "icon": {
        "pos": (self.pos[0]+5,self.pos[1]+5),
        "size": (50,50)
      }
    }
    return data
  
  def setup(self):
    data = self.calculateItemPositionsAndSize()
    print(data)
    self.button.update(self.pos, self.size)
    self.title.update(data["title"]["pos"], data["title"]["size"])
    self.description.update(data["description"]["pos"], data["description"]["size"])
    self.icon.update(data["icon"]["pos"], data["icon"]["size"])


  def purchase(self):
    self.gameCon.makePurchase(self.itemData["cost"], self.itemData)

  def render(self, surface, events):
    self.button.render(surface, events)
    self.icon.render(surface)
    self.title.render(surface)
    self.description.render(surface)

  def update(self, pos, size):
    self.pos = pos
    self.size = size
    self.setup()