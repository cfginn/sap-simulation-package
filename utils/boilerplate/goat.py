
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Goat(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend bought: Gain 1 gold.
    # lvl 2: Friend bought: Gain 1 gold.
    # lvl 3: Friend bought: Gain 1 gold.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.BUY, constants.EACH_FRIEND, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.GOAT, tier = 5, ability=self.ability)

      