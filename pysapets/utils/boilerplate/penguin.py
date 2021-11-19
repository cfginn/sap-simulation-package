
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Penguin(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: Give other Lvl. 2 and 3 friends +1/+1
    # lvl 2: End turn: Give other Lvl. 2 and 3 friends +2/+2
    # lvl 3: End turn: Give other Lvl. 2 and 3 friends +3/+3
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.PENGUIN, tier = 4, ability=self.ability)

      