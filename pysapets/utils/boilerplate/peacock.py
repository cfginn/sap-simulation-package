
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Peacock(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Hurt: Gain 2 Attack.
    # lvl 2: Hurt: Gain 4 Attack.
    # lvl 3: Hurt: Gain 6 Attack.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.HURT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.PEACOCK, tier = 2, ability=self.ability)

      