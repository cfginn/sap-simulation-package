class Animal:
  # init health and attack  
  def __init__(self, health, attack):
    self.health = health
    self.attack = attack
    self.dead = False
    self.level = 1
     
  # hurt the animal
  def hurt(self, damage):
    self.health -= damage
    if self.health < 0:
      self.health = 0
      self.dead = True

  # check if the animal is dead
  def is_dead(self):
    return self.dead
    
  # attack the animal
  def attack(self, target):
    target.hurt(self.attack)

  # get the health of the animal
  def get_health(self):
    return self.health
  
  # get the attack of the animal
  def get_attack(self):
    return self.attack
    
  # feed animal food
  def feed(self, food):
    self.health += food.get_health()
    self.attack += food.get_attack()

    if self.health > 50:
      self.health = 50
    
    if self.attack > 50:
      self.attack = 50
    
  