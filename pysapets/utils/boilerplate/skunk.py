
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Skunk(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of battle: Reduce the highest Health enemy by 33%.
    # lvl 2: Start of battle: Reduce the highest Health enemy by 66%.
    # lvl 3: Start of battle: Reduce the highest Health enemy by 100%.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SKUNK, tier = 4, ability=self.ability)

      