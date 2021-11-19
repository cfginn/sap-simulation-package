
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Spider(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Summon one tier 3 animal as a 2/2.
    # lvl 2: Faint: Summon one tier 3 animal as a 4/4.
    # lvl 3: Faint: Summon one tier 3 animal as a 6/6.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SPIDER, tier = 2, ability=self.ability)

      