class GameCon:
  def __init__(self, data = (0,0,0)):
    self.cash=data[0]
    self.followersPerSecond=data[1]
    self.Followers=data[2]
    self.items = {}

  def getCash(self):
    return round(self.cash, 2)
  def getfollowersPerSecond(self):
    return round(self.followersPerSecond, 2)
  def getFollowers(self):
    return round(self.Followers, 2)

  def updateCash(self, ammount):
    self.cash += round(ammount, 2)
  def updatefollowersPerSecond(self, ammount):
    self.followersPerSecond += round(ammount, 2)
  def updateFollowers(self, ammount):
    self.Followers += round(ammount, 2)

  def setCash(self, value):
    self.cash = round(value, 2)
  def setfollowersPerSecond(self, value):
    self.followersPerSecond = round(value, 2)
  def setFollowers(self, value):
    self.Followers = round(value, 2)

  def makePurchase(self, item):
    cost = item['cost']
    follows = item['follows']
    canBuy = (self.getCash() - cost) >= 0
    if canBuy:
      if item["id"] in self.items:
        self.items[item["id"]] += 1
        #cost = cost * (self.items[item["id"]] * .5)
      else:
        self.items[item["id"]] = 1
      self.updateCash(-cost)
      self.updateFollowers(-follows)
      self.updatefollowersPerSecond(item["fps"])

  def useFPS(self):
    self.updateFollowers(self.getfollowersPerSecond())

  def getData(self):
    return (self.data, self.followersPerSecond, self.Followers)