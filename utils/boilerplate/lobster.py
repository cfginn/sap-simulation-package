
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Lobster(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend summoned: Give it +2/+2 when not in battle.
    # lvl 2: Friend summoned: Give it +4/+4 when not in battle.
    # lvl 3: Friend summoned: Give it +6/+6 when not in battle.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.SUMMONED, constants.EACH_FRIEND, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.LOBSTER, tier = 4, ability=self.ability)

      