
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Dragon(Animal):
  # base health and attack values
  BASE_ATTACK = 6 
  BASE_HEALTH = 8 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Buy tier 1 animal: Give all friends +1/+1.
    # lvl 2: Buy tier 1 animal: Give all friends +2/+2.
    # lvl 3: Buy tier 1 animal: Give all friends +3/+3.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.BUY_TIER_1_ANIMAL, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.DRAGON, tier = 6, ability=self.ability)

      