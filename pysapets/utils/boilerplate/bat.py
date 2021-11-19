
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Bat(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of battle: Make 1 enemy Weak.
    # lvl 2: Start of battle: Make 2 enemies Weak.
    # lvl 3: Start of battle: Make 3 enemies Weak.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.BAT, tier = 2, ability=self.ability)

      