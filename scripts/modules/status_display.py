from ..components.text import TextBox as Tb

class Status:
  def __init__(self, gameCon, pos, size):
    self.gameCon = gameCon
    self.pos = pos
    self.size = size
    self.setup()
  
  def render(self, surface):
    self.updateText()
    self.moral.render(surface)
    self.cash.render(surface)
    self.follows.render(surface)
    
  
  def setup(self):
    (pos, size) = self.calcTextPosNSize(3, self.pos, self.size, 5)
    (textColor, backgroundColor) = ((255,255,255), (130,90,130))
    textsize = 22
    textCentering = (True, False)
    self.moral = Tb(pos[0], size[0], f'CPS: {self.gameCon.getClicksPerSecond()}', textColor, backgroundColor, textCentering, textsize)
    self.cash = Tb(pos[1], size[1], f'Cash: {self.gameCon.getCash()}', textColor, backgroundColor, textCentering, textsize)
    self.follows = Tb(pos[2], size[2], f'Follows: {self.gameCon.getFollowers()}', textColor, backgroundColor, textCentering, textsize)
  
  def updateText(self):
    self.moral.text = f'CPS: {self.gameCon.getClicksPerSecond()}'
    self.cash.text = f'Cash: {self.gameCon.getCash()}'
    self.follows.text = f'Follows: {self.gameCon.getFollowers()}'
  
  def update(self, pos, size):
    self.pos = pos
    self.size = size
    self.setup()

  def calcTextPosNSize(self, numOButtons, offest, scale, padding):
    # Calculate the positions of buttons
    pos = []
    size = []
    cx = offest[0]
    wid = ((scale[0] - ((numOButtons - 1) * padding)) // numOButtons)
    for i in range(0, numOButtons):
      pos.append((cx, offest[1]))
      size.append((wid, scale[1]))
      cx += (wid + padding)
    return (pos, size)