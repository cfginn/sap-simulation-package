
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Sauropod(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 12 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Buy food: Gain 1 gold.
    # lvl 2: Buy food: Gain 1 gold.
    # lvl 3: Buy food: Gain 1 gold.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.BUY_FOOD, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SAUROPOD, tier = 6, ability=self.ability)

      