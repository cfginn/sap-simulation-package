
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Snail(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Buy: If you lost last battle, give all friends +2/+1
    # lvl 2: Buy: If you lost last battle, give all friends +4/+2
    # lvl 3: Buy: If you lost last battle, give all friends +6/+3
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.BUY_AFTER_LOSS, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SNAIL, tier = 3, ability=self.ability)

      