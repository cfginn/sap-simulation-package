# define food class

class Food:
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack
    self.bought = False
  
  # getters
  def get_name(self):
    return self.name
  def get_health(self):
    return self.health
  def get_attack(self):
    return self.attack
  
  # buy item 
  def buy(self):
    self.bought = True