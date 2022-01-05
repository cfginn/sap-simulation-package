
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Badger(Animal):
  # base health and attack values
  BASE_ATTACK = 5 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Deal Attack damage to adjacent animals
    # lvl 2: Faint: Deal Attack damage to adjacent animals
    # lvl 3: Faint: Deal Attack damage to adjacent animals
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.EATS_SHOP_FOOD, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.BADGER, tier = 3, ability=self.ability)

      