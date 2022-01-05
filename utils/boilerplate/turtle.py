
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Turtle(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Give friend behind Melon Armor
    # lvl 2: Faint: Give 2 friends behind Melon Armor
    # lvl 3: Faint: Give 3 friends behind Melon Armor
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.TURTLE, tier = 3, ability=self.ability)

      