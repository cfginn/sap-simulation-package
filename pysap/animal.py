class Animal:
  # define ability class
  class Ability:
    # constructor
    def __init__(self, trigger, triggeredBy, triggeredByN, effectFunction):
      self.trigger = trigger
      self.triggeredBy = triggeredBy
      self.triggeredByN = triggeredByN
      self.effectFunction = effectFunction


#******************************************************************************** 
  # animal class
  # init health and attack  
  def __init__(self, baseAttack, baseHealth, animalType = None, tier = 1, status = None, ability = None):
    self.health = baseHealth
    self.attack = baseAttack
    self.type = animalType
    self.dead = False
    self.level = 1
    self.experience = 0
    self.tier = tier
    self.status = status
    self.ability = ability
    
  # get the health of the animal
  def get_health(self):
    return self.health
  
  # get the attack of the animal
  def get_attack(self):
    return self.attack
  # get the type of the animal
  def get_type(self):
    return self.type

  # get whether the animal is dead
  def is_dead(self):
    return self.dead  

  # get the level of the animal
  def get_level(self):
    return self.level

  # get the experience of the animal
  def get_experience(self):
    return self.experience

  # get the tier of the animal
  def get_tier(self):
    return self.tier

  # get the status of the animal
  def get_status(self):
    return self.status
  
  # add experience to the animal
  def add_experience(self, experience):
    self.experience += experience

    if self.experience >= 2:
      self.level = 2

    if self.experience == 5:
      self.level = 3
    
    if self.experience > 5:
      self.experience = 5
  
  # add health to the animal
  def add_health(self, health):
    self.health += health

  # subtract health from the animal
  def subtract_health(self, health):
    self.health -= health

    if self.health <= 0:
      self.health = 0
      self.dead = True

  # add attack to the animal
  def add_attack(self, attack):
    self.attack += attack

  # add status to the animal
  def add_status(self, status):
    self.status = status
  
  # remove status from the animal
  def remove_status(self):
    self.status = None