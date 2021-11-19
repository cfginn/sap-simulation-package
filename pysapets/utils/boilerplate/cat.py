
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Cat(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Food with Health and Attack effects are doubled.
    # lvl 2: Food with Health and Attack effects are tripled.
    # lvl 3: Food with Health and Attack effects are quadrupled.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.HURT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.CAT, tier = 6, ability=self.ability)

      