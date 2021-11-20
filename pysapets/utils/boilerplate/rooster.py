
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Rooster(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Summon a Chick with the same Attack as this.
    # lvl 2: Faint: Summon 2 Chicks with the same Attack as this.
    # lvl 3: Faint: Summon 3 Chicks with the same Attack as this.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.ROOSTER, tier = 4, ability=self.ability)

      