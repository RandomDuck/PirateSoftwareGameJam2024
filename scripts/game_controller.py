class GameCon:
  def __init__(self, data = (0,0,0)):
    self.cash=data[0]
    self.clicksPerSecond=data[1] #TODO: MAKE CPS do something
    self.credibility=data[2]
    self.items = {}

  def getCash(self):
    return self.cash
  def getClicksPerSecond(self):
    return self.clicksPerSecond
  def getCredibility(self):
    return self.credibility

  def updateCash(self, ammount):
    self.cash += ammount
  def updateClicksPerSecond(self, ammount):
    self.clicksPerSecond += ammount
  def updateCredibility(self, ammount):
    self.credibility += ammount

  def setCash(self, value):
    self.cash = value
  def setClicksPerSecond(self, value):
    self.clicksPerSecond = value
  def setCredibility(self, value):
    self.credibility = value

  def makePurchase(self, item):
    cost = item['cost']
    cred = item['cred']
    canBuy = (self.getCash() - cost) >= 0
    if canBuy:
      if item["id"] in self.items:
        self.items[item["id"]] += 1
      else:
        self.items[item["id"]] = 1
      self.updateCash(-cost)
      self.updateCredibility(-cred)
      self.updateClicksPerSecond(item["cps"])

  def getData(self):
    return (self.data, self.clicksPerSecond, self.credibility)