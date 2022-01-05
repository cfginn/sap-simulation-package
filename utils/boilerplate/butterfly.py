
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Butterfly(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 1 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Copy stats of the strongest friend (highest attack and health combined).
    # lvl 2: End turn: If you have 3 or more gold, give other friends +4/+4
    # lvl 3: End turn: If you have 3 or more gold, give other friends +6/+6
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.SUMMONED, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.BUTTERFLY, tier = Summoned, ability=self.ability)

      