
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Mammoth(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 6 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Give all friends +2/+2
    # lvl 2: Faint: Give all friends +4/+4
    # lvl 3: Faint: Give all friends +6/+6
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.MAMMOTH, tier = 6, ability=self.ability)

      