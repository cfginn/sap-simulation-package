
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Cricket(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Summon a 1/1 Cricket
    # lvl 2: Faint: Summon a 2/2 Cricket
    # lvl 3: Faint: Summon a 3/3 Cricket
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.CRICKET, tier = 1, ability=self.ability)

      