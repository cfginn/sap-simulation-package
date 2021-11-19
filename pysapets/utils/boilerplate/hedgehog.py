
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Hedgehog(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Deal 2 damage to all.
    # lvl 2: Faint: Deal 4 damage to all.
    # lvl 3: Faint: Deal 6 damage to all.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.HEDGEHOG, tier = 2, ability=self.ability)

      