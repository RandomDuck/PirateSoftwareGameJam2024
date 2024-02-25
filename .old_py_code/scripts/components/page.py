class Page:
  def __init__(self, screen, area, gameCon):
    self.screen = screen
    self.pos = area[0]
    self.size = area[1]
    self.gameCon = gameCon
    self.elements = []
    self.buttons = []

  def render(self, events):
    screen = self.screen
    for element in self.elements:
      element.render(screen)
    for button in self.buttons:
      button.render(screen, events)

  def update(self, area):
    self.pos = area[0]
    self.size = area[1]

  def calcEvenDist(self, itemNum, offset, width, padding=0):
    pos = []
    size = []
    cx = offset
    wid = ((width - ((itemNum - 1) * padding)) // itemNum)
    for i in range(0, itemNum):
      pos.append(cx)
      size.append(wid)
      cx += (wid + padding)
    return (pos, size)

  def calcEvenDistMargin(self, itemNum, offset, width, padding=0):
    return self.calcEvenDist(itemNum, offset, (width-offset), padding)