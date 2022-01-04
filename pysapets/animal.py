class Animal:
  # define ability class
  class Ability:
    # constructor
    def __init__(self, animal, trigger, triggeredBy, effectFunction, triggeredByN = None):
      self.animal = animal
      self.trigger = trigger
      self.triggeredBy = triggeredBy
      self.triggeredByN = triggeredByN
      self.effectFunction = effectFunction

    # get ability trigger
    def get_trigger(self):
      return self.trigger
    
    # get ability triggeredBy
    def get_triggeredBy(self):
      return self.triggeredBy
    
    # get ability triggeredByN
    def get_triggeredByN(self):
      return self.triggeredByN
    
    # get ability effectFunction
    def get_effectFunction(self):
      return self.effectFunction


#******************************************************************************** 
  # animal class
  # init health and attack  
  def __init__(self, baseAttack, baseHealth, animalType = "Animal", tier = 1, status = None, ability = None):
    self.health = baseHealth
    self.attack = baseAttack
    self.animalType = animalType
    self.dead = False
    self.level = 1
    self.experience = 0
    self.tier = tier
    self.status = status
    self.ability = ability
  
  # define __str__
  def __str__(self):
    # return "{}: level {}, attack {}, health {}, exp {}".format(self.animalType, self.level, self.attack, self.health, self.experience)
    return "{}(A: {}, H: {}, L: {}, E: {})".format(self.animalType, self.attack, self.health, self.level, self.experience)
  
  def __repr__(self):
    # return "{}: level {}, attack {}, health {}, exp {}".format(self.animalType, self.level, self.attack, self.health, self.experience)
    return "{}(A: {}, H: {}, L: {}, E: {})".format(self.animalType, self.attack, self.health, self.level, self.experience)
  # get the health of the animal
  def get_health(self):
    return self.health
  
  # get the attack of the animal
  def get_attack(self):
    return self.attack
  # get the animalType of the animal
  def get_type(self):
    return self.animalType

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

  # run ability
  def run_ability(self, **kwargs):
    if self.ability:
      self.ability.effectFunction(self, **kwargs)
  
  # get ability trigger
  def get_ability_trigger(self):
    if self.ability:
      return self.ability.get_trigger()
  
  # get ability triggeredBy
  def get_ability_triggeredBy(self):
    if self.ability:
      return self.ability.get_triggeredBy()

  # get ability triggeredByN
  def get_ability_triggeredByN(self):
    if self.ability:
      return self.ability.get_triggeredByN()

  # get ability effectFunction
  def get_ability_effectFunction(self):
    if self.ability:
      return self.ability.get_effectFunction()