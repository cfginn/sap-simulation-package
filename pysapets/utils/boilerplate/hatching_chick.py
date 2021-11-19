
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Hatching_chick(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 1 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: Give +5/+5 to friend ahead until end of battle.
    # lvl 2: End turn: Give +2/+2 to friend ahead.
    # lvl 3: Start of turn: Give +1 Experience to friend ahead
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.HATCHING_CHICK, tier = 3, ability=self.ability)

      