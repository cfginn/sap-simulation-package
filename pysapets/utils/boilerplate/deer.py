
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Deer(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 1 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Summon a 5/5 Bus with Splash Attack
    # lvl 2: Faint: Summon a 10/10 Bus with Splash Attack
    # lvl 3: Faint: Summon a 15/15 Bus with Splash Attack
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.DEER, tier = 4, ability=self.ability)

      