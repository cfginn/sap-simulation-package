
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Horse(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 1 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend summoned: Give it +1 Attack until end of battle
    # lvl 2: Friend summoned: Give it +2 Attack until end of battle
    # lvl 3: Friend summoned: Give it +3 Attack until end of battle
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.SUMMONED, constants.EACH_FRIEND, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.HORSE, tier = 1, ability=self.ability)

      