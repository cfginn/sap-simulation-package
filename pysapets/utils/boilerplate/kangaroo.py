
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Kangaroo(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend ahead attacks: Gain +2/+2
    # lvl 2: Friend ahead attacks: Gain +4/+4
    # lvl 3: Friend ahead attacks: Gain +6/+6
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.AFTER_ATTACK, constants.FRIEND_AHEAD, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.KANGAROO, tier = 3, ability=self.ability)

      