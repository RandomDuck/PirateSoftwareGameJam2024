class GameCon:
  def __init__(self, data = (0,0,0)):
    self.cash=data[0]
    self.morality=data[1]
    self.credibility=data[2]

  def getCash(self):
    return self.cash
  def getMorality(self):
    return self.morality
  def getCredibility(self):
    return self.credibility

  def updateCash(self, ammount):
    self.cash += ammount
  def updateMorality(self, ammount):
    self.morality += ammount
  def updateCredibility(self, ammount):
    self.credibility += ammount

  def setCash(self, value):
    self.cash = value
  def setMorality(self, value):
    self.morality = value
  def setCredibility(self, value):
    self.credibility = value
