
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Whale(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 6 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of battle: Swallow friend ahead and release it as a level 1 after fainting.
    # lvl 2: Start of battle: Swallow friend ahead and release it as a level 2 after fainting.
    # lvl 3: Start of battle: Swallow friend ahead and release it as a level 3 after fainting.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.WHALE, tier = 3, ability=self.ability)

      