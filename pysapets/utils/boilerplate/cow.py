
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Cow(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 6 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Buy: Replace food shop with 2 free milk that gives +2/+2.
    # lvl 2: Buy: Replace food shop with 2 free milk that gives +2/+2.
    # lvl 3: Buy: Replace food shop with 2 free milk that gives +2/+2.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.BUY, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.COW, tier = 5, ability=self.ability)

      