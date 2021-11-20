
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Elephant(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Before Attack: Deal 1 damage to 1 friends behind.
    # lvl 2: Before Attack: Deal 1 damage to 2 friends behind.
    # lvl 3: Before Attack: Deal 1 damage to 3 friends behind.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.BEFORE_ATTACK, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.ELEPHANT, tier = 2, ability=self.ability)

      