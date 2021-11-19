
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Shrimp(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 1 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend sold: Give a random friend +1 Health.
    # lvl 2: Friend sold: Give a random friend +2 Health.
    # lvl 3: Friend sold: Give a random friend +3 Health.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.SELL, constants.EACH_FRIEND, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SHRIMP, tier = 2, ability=self.ability)

      