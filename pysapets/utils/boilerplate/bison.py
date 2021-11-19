
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Bison(Animal):
  # base health and attack values
  BASE_ATTACK = 6 
  BASE_HEALTH = 6 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: Gain +2/+2 if there is at least one Lvl. 3 friend.
    # lvl 2: End turn: Gain +4/+4 if there is at least one Lvl. 3 friend.
    # lvl 3: End turn: Gain +6/+6 if there is at least one Lvl. 3 friend.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN_WITH_LVL_3_FRIEND, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.BISON, tier = 4, ability=self.ability)

      