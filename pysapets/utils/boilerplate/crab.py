
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Crab(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of battle: Copy Health from friend ahead.
    # lvl 2: Start of battle: Copy Health from friend ahead.
    # lvl 3: Start of battle: Copy Health from friend ahead.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.CRAB, tier = 2, ability=self.ability)

      