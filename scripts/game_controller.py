class GameCon:
  def __init__(self, data = (0,0,0)):
    self.cash=data[0]
    self.clicksPerSecond=data[1]
    self.credibility=data[2]

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

  def getData(self):
    return (self.data, self.clicksPerSecond, self.credibility)