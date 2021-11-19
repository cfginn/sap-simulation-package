
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Octopus(Animal):
  # base health and attack values
  BASE_ATTACK = 8 
  BASE_HEALTH = 8 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Level-up: Gain +8/+8.
    # lvl 2: Level-up: Gain +8/+8 and a new ability.
    # lvl 3: Before attack: Deal 5 damage to all enemies
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.LEVEL_UP, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.OCTOPUS, tier = 6, ability=self.ability)

      