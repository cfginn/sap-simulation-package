
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Rat(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: summon one 1/1 Dirty Rat for the opponent that betrays him.
    # lvl 2: Faint: summon one 1/1 Dirty Rat for the opponent that betrays him.
    # lvl 3: Faint: summon one 1/1 Dirty Rat for the opponent that betrays him.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.RAT, tier = 2, ability=self.ability)

      