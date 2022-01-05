
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Giraffe(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: Give friend ahead +1/+1
    # lvl 2: End turn: Give 2 friends ahead +1/+1
    # lvl 3: End turn: Give 3 friends ahead +1/+1
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.GIRAFFE, tier = 3, ability=self.ability)

      