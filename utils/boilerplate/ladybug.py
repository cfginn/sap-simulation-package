
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Ladybug(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Buy food: Gain +1/+1 until end of battle
    # lvl 2: Buy food: Gain +2/+2 until end of battle
    # lvl 3: Buy food: Gain +3/+3 until end of battle
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.BUY_FOOD, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.LADYBUG, tier = 1, ability=self.ability)

      