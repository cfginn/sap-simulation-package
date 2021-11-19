
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Sheep(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Summon two 2/2 Rams
    # lvl 2: Faint: Summon two 4/4 Rams
    # lvl 3: Faint: Summon two 6/6 Rams
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SHEEP, tier = 3, ability=self.ability)

      