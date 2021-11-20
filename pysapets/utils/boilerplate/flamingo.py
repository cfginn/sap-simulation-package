
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Flamingo(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 1 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Give the two friends behind +1/+1.
    # lvl 2: Faint: Give the two friends behind +2/+2.
    # lvl 3: Faint: Give the two friends behind +3/+3.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.FLAMINGO, tier = 2, ability=self.ability)

      