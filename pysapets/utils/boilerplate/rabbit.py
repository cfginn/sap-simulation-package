
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Rabbit(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend eats shop food: Give it +1 Health
    # lvl 2: Friend eats shop food: Give it +2 Health
    # lvl 3: Friend eats shop food: Give it +3 Health
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.EATS_SHOP_FOOD, constants.EACH_FRIEND, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.RABBIT, tier = 3, ability=self.ability)

      