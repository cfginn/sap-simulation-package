
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Turkey(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend summoned: Give it +3/+3.
    # lvl 2: Friend summoned: Give it +6/+6.
    # lvl 3: Friend summoned: Give it +9/+9.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.SUMMONED, constants.EACH_FRIEND, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.TURKEY, tier = 5, ability=self.ability)

      