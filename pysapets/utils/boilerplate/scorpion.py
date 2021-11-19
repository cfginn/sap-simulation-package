
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Scorpion(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 1 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Knock out: Deal 4 damage to the first enemy.
    # lvl 2: Knock out: Deal 8 damage to the first enemy.
    # lvl 3: Knock out: Deal 12 damage to the first enemy.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.KNOCK_OUT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SCORPION, tier = 5, ability=self.ability)

      