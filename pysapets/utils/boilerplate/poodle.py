
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Poodle(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: Give +1/+1 to different tier animals.
    # lvl 2: End turn: Give +2/+2 to different tier animals.
    # lvl 3: End turn: Give +3/+3 to different tier animals.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.POODLE, tier = 4, ability=self.ability)

      