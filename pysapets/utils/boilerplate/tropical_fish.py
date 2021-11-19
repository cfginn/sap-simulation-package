
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Tropical_fish(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End turn: Give adjacent friends +1 Health
    # lvl 2: End turn: Give adjacent friends +2 Health
    # lvl 3: End turn: Give adjacent friends +3 Health
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.TROPICAL_FISH, tier = 3, ability=self.ability)

      