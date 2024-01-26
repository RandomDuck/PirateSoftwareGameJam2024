class GameCon:
  def __init__(self, data = (0,0,0)):
    self.cash=data[0]
    self.followersPerSecond=data[1] #TODO: MAKE fps do something
    self.Followers=data[2]
    self.items = {}

  def getCash(self):
    return self.cash
  def getfollowersPerSecond(self):
    return self.followersPerSecond
  def getFollowers(self):
    return self.Followers

  def updateCash(self, ammount):
    self.cash += ammount
  def updatefollowersPerSecond(self, ammount):
    self.followersPerSecond += ammount
  def updateFollowers(self, ammount):
    self.Followers += ammount

  def setCash(self, value):
    self.cash = value
  def setfollowersPerSecond(self, value):
    self.followersPerSecond = value
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
      self.updatefollowersPerSecond(item["fps"])

  def getData(self):
    return (self.data, self.followersPerSecond, self.Followers)