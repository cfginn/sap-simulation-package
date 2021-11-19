
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Ram(Animal):
  # base health and attack values
  BASE_ATTACK = ? 
  BASE_HEALTH = ? 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: If you have 3 or more gold, give other friends +2/+2
    # lvl 2: End turn: If you have 3 or more gold, give other friends +4/+4
    # lvl 3: End turn: If you have 3 or more gold, give other friends +6/+6
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN_WITH_3_PLUS_GOLD, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.RAM, tier = Summoned, ability=self.ability)

      