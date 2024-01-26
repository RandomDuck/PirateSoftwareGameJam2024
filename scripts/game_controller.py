class GameCon:
  def __init__(self, data = (0,0,0)):
    self.cash=data[0]
    self.clicksPerSecond=data[1] #TODO: MAKE CPS do something
    self.Followers=data[2]
    self.items = {}

  def getCash(self):
    return self.cash
  def getClicksPerSecond(self):
    return self.clicksPerSecond
  def getFollowers(self):
    return self.Followers

  def updateCash(self, ammount):
    self.cash += ammount
  def updateClicksPerSecond(self, ammount):
    self.clicksPerSecond += ammount
  def updateFollowers(self, ammount):
    self.Followers += ammount

  def setCash(self, value):
    self.cash = value
  def setClicksPerSecond(self, value):
    self.clicksPerSecond = value
  def setFollowers(self, value):
    self.Followers = value

  def makePurchase(self, item):
    cost = item['cost']
    follows = item['follows']
    canBuy = (self.getCash() - cost) >= 0
    if canBuy:
      if item["id"] in self.items:
        self.items[item["id"]] += 1
      else:
        self.items[item["id"]] = 1
      self.updateCash(-cost)
      self.updateFollowers(-follows)
      self.updateClicksPerSecond(item["cps"])

  def getData(self):
    return (self.data, self.clicksPerSecond, self.Followers)