
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Gorilla(Animal):
  # base health and attack values
  BASE_ATTACK = 6 
  BASE_HEALTH = 6 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Hurt: Gain Coconut Shield.
    # lvl 2: Hurt: Gain Coconut Shield.
    # lvl 3: Hurt: Gain Coconut Shield.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.HURT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.GORILLA, tier = 6, ability=self.ability)

      