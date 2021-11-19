
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Llama(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: If you have 4 or less animals, gain +2/+2.
    # lvl 2: End turn: If you have 4 or less animals, gain +4/+4.
    # lvl 3: End turn: If you have 4 or less animals, gain +6/+6.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN_WITH_4_OR_LESS_ANIMALS, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.LLAMA, tier = 4, ability=self.ability)

      