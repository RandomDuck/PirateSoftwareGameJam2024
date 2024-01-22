from ..components.text import TextBox as Tb

class Status:
  def __init__(self, gameCon, pos, size):
    self.gameCon = gameCon
    self.pos = pos
    self.size = size
    self.setup()
  
  def render(self, surface):
    self.moral.render(surface)
    self.cash.render(surface)
    self.cred.render(surface)
    
  
  def setup(self):
    (pos, size) = self.calcTextPosNSize(3, self.pos, self.size, 5)
    (textColor, backgroundColor) = ((255,255,255), (90,90,90))
    textsize = 22
    textCentering = (True, False)
    self.moral = Tb(pos[0], size[0], f'Moral: {self.gameCon.getMorality()}', textColor, backgroundColor, textCentering, textsize)
    self.cash = Tb(pos[1], size[1], f'Cash: {self.gameCon.getCash()}', textColor, backgroundColor, textCentering, textsize)
    self.cred = Tb(pos[2], size[2], f'Cred: {self.gameCon.getCredibility()}', textColor, backgroundColor, textCentering, textsize)
  
  def updateText(self):
    self.moral.text = f'Moral: {self.gameCon.getMorality()}'
    self.cash.text = f'Cash: {self.gameCon.getCash()}'
    self.cred.text = f'Cred: {self.gameCon.getCredibility()}'
  
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