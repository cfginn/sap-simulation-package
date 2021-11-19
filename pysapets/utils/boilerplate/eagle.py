
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Eagle(Animal):
  # base health and attack values
  BASE_ATTACK = 6 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Summon one Lvl. 1 tier 6 animal.
    # lvl 2: Faint: Summon one Lvl. 2 tier 6 animal.
    # lvl 3: Faint: Summon one Lvl. 3 tier 6 animal.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.EAGLE, tier = 5, ability=self.ability)

      