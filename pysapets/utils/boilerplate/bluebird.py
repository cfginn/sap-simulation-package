
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Bluebird(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 1 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: Give left-most friend +1 attack
    # lvl 2: End turn: Give left-most friend +2 attack
    # lvl 3: End turn: Give left-most friend +3 attack
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.BLUEBIRD, tier = 1, ability=self.ability)

      