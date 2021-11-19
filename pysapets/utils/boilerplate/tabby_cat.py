
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Tabby_cat(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Eats shop food: Give friends +1 Attack until end of battle
    # lvl 2: Eats shop food: Give friends +2 Attack until end of battle
    # lvl 3: Eats shop food: Give friends +3 Attack until end of battle
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.EATS_SHOP_FOOD, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.TABBY_CAT, tier = 2, ability=self.ability)

      