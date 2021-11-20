
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Dodo(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of battle: Give Attack to friend ahead.
    # lvl 2: Start of battle: Give 2X Attack to friend ahead.
    # lvl 3: Start of battle: Give 3X Attack to friend ahead.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.DODO, tier = 2, ability=self.ability)

      