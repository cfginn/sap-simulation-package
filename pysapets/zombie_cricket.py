
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class ZombieCricket(Animal):
  # base health and attack values
  
  def __init__(self, cricket, addAttack = 0, addHealth = 0):
    self.BASE_ATTACK = cricket.level
    self.BASE_HEALTH = cricket.level

    # does not have an ability
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, None, None, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.ZOMBIE_CRICKET, tier = "Summoned", ability=self.ability)

      