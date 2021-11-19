
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Microbe(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 1 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Make all animals Weak.
    # lvl 2: Faint: Make all animals Weak.
    # lvl 3: Faint: Make all animals Weak.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.MICROBE, tier = 5, ability=self.ability)

      