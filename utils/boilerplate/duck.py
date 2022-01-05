
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Duck(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Sell: Give shop animals +1/+1
    # lvl 2: Sell: Give shop animals +2/+2
    # lvl 3: Sell: Give shop animals +3/+3
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.SELL, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.DUCK, tier = 1, ability=self.ability)

      