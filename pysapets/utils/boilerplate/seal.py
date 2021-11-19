
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Seal(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 6 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Eats shop food: Give 2 random friends +1/+1.
    # lvl 2: Eats shop food: Give 2 random friends +2/+2.
    # lvl 3: Eats shop food: Give 2 random friends +3/+3.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.EATS_SHOP_FOOD, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SEAL, tier = 5, ability=self.ability)

      