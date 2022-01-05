
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Beetle(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Eat shop food: Give shop animals +1 health
    # lvl 2: Eat shop food: Give shop animals +2 health
    # lvl 3: Eat shop food: Give shop animals +3 health
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.EATS_SHOP_FOOD, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.BEETLE, tier = 1, ability=self.ability)

      