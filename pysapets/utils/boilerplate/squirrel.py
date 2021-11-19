
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Squirrel(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Buy: Clear and fill shops with food.
    # lvl 2: Buy: Clear and fill shops with food.
    # lvl 3: Buy: Clear and fill shops with food.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.LEVEL_UP, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SQUIRREL, tier = 4, ability=self.ability)

      