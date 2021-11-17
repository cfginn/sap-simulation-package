# def game class

class Game:
  # constructor
  def __init__(self):
    self.gold = 10
    self.health = 10
    self.turn = 0
    self.wins = 0
    self.team = []
    self.store = []
  
  # getters
  def get_gold(self):
    return self.gold
  def get_health(self):
    return self.health
  def get_turn(self):
    return self.turn
  def get_wins(self):
    return self.wins

  # buy item
  def buy(self, item):
    if self.gold >= item.cost:
      self.gold -= item.cost
      item.bought = True
      return True
    else:
      return False
    
  # sell item
  def sell(self, item):
    self.gold += item.cost
    item.bought = False

    return True
  
  def fill_shop(self):
    pass

  # start turn
  def start_turn(self):
    self.turn += 1
    self.gold = 10

    self.fill_shop()

  # end turn
  def end_turn(self):
    pass 
  
  # run battle
  def battle(self, enemy):
    pass

  # end battle
  def end_battle(self):
    pass

  # handle loss
  def lose(self):
    # lose one health on first two turns, two on next two, three for rest
    health_lost = self.turn // 2 + 1
    if self.turn > 3:
      health_lost = 3

    self.health -= health_lost

    self.turn += 1
  
  # handle win
  def win(self):
    self.wins += 1
    self.turn += 1


  

  
