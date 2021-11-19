
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Buffalo(Animal):
  # base health and attack values
  BASE_ATTACK = 5 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend bought: Gain +1/+1
    # lvl 2: Friend bought: Gain +2/+2
    # lvl 3: Friend bought: Gain +3/+3
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.BUY, constants.EACH_FRIEND, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.BUFFALO, tier = 4, ability=self.ability)

      