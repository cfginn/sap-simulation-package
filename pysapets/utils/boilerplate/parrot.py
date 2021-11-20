
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Parrot(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: End Turn: Copy ability from pet ahead as lvl. 1 until end of battle.
    # lvl 2: End Turn: Copy ability from pet ahead as lvl. 2 until end of battle.
    # lvl 3: End Turn: Copy ability from pet ahead as lvl. 3 until end of battle.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.END_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.PARROT, tier = 5, ability=self.ability)

      