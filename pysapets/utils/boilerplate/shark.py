
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Shark(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend faints: Gain +2/+1.
    # lvl 2: Friend faints: Gain +4/+2.
    # lvl 3: Friend faints: Gain +6/+3.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.EACH_FRIEND, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SHARK, tier = 5, ability=self.ability)

      