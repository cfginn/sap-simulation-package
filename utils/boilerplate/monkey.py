
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Monkey(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: Give right-most friend +2/+2
    # lvl 2: End turn: Give right-most friend +4/+4
    # lvl 3: End turn: Give right-most friend +6/+6
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.MONKEY, tier = 4, ability=self.ability)

      