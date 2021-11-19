
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Hippo(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 7 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Knock out: Gain +2/+2.
    # lvl 2: Knock out: Gain +4/+4.
    # lvl 3: Knock out: Gain +6/+6.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.KNOCK_OUT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.HIPPO, tier = 4, ability=self.ability)

      