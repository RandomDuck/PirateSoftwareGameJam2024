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
    cash = self.itemData['cost']
    follows = self.itemData['follows']
    fps = self.itemData['fps']
    self.costText = Text(pos,size, f"Cash: {'-' if cash > 0 else '' if cash == 0 else '+'}{cash if cash > 0 else -cash}", (255,255,255), (True,False), 22)
    self.followsText = Text(pos,size, f"follows: {'-' if follows > 0 else '' if follows == 0 else '+'}{follows if follows > 0 else -follows}", (255,255,255), (True,False), 22)
    self.fpsText = Text(pos,size, f"FPS: {'+' if fps > 0 else '' if fps == 0 else '-'}{fps if fps > 0 else -fps}", (255,255,255), (True,False), 22)
    self.icon = Icon(self.itemData["iconPath"], pos, size)
    self.setup()

  def calculateItemPositionsAndSize(self):
    nameWidth = 0.7
    infoWidth = 0.3
    data = {
      "title": {
        "pos": (self.pos[0]+65, self.pos[1]+10),
        "size": (self.size[0]*nameWidth,20)
      },
      "description": {
        "pos": (self.pos[0]+65, self.pos[1]+35),
        "size": (self.size[0]*nameWidth,20)
      },
      "follows": {
        "pos": (self.pos[0]+65+(self.size[0]*nameWidth), self.pos[1]+5),
        "size": (self.size[0]*infoWidth,20)
      },
      "cost": {
        "pos": (self.pos[0]+65+(self.size[0]*nameWidth), self.pos[1]+20),
        "size": (self.size[0]*infoWidth,20)
      },
      "fps": {
        "pos": (self.pos[0]+65+(self.size[0]*nameWidth), self.pos[1]+35),
        "size": (self.size[0]*infoWidth,20)
      },
      "icon": {
        "pos": (self.pos[0]+5,self.pos[1]+5),
        "size": (50,50)
      }
    }
    return data
  
  def setup(self):
    data = self.calculateItemPositionsAndSize()
    self.button.update(self.pos, self.size)
    self.title.update(data["title"]["pos"], data["title"]["size"])
    self.description.update(data["description"]["pos"], data["description"]["size"])
    self.followsText.update(data["follows"]["pos"], data["description"]["size"])
    self.costText.update(data["cost"]["pos"], data["description"]["size"])
    self.fpsText.update(data["fps"]["pos"], data["description"]["size"])
    self.icon.update(data["icon"]["pos"], data["icon"]["size"])


  def purchase(self):
    self.gameCon.makePurchase(self.itemData)

  def render(self, surface, events):
    self.button.render(surface, events)
    self.icon.render(surface)
    self.title.render(surface)
    self.description.render(surface)
    self.followsText.render(surface)
    self.fpsText.render(surface)
    self.costText.render(surface)

  def update(self, pos, size):
    self.pos = pos
    self.size = size
    self.setup()