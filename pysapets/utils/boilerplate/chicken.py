
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Chicken(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Buy tier 1 animal: Give current and future shop animals +1/+1
    # lvl 2: Buy tier 1 animal: Give current and future shop animals +2/+2
    # lvl 3: Buy tier 1 animal: Give current and future shop animals +3/+3
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.BUY_TIER_1_ANIMAL, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.CHICKEN, tier = 5, ability=self.ability)

      