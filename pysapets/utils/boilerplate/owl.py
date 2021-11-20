
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Owl(Animal):
  # base health and attack values
  BASE_ATTACK = 5 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Sell: Give a random friend +2/+2
    # lvl 2: Sell: Give a random friend +2/+2
    # lvl 3: Sell: Give a random friend +2/+2
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.SELL, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.OWL, tier = 3, ability=self.ability)

      