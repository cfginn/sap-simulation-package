
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Pig(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Sell: Gain an extra 1 gold
    # lvl 2: Sell: Gain an extra 2 gold
    # lvl 3: Sell: Gain an extra 3 gold
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.SELL, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.PIG, tier = 1, ability=self.ability)

      