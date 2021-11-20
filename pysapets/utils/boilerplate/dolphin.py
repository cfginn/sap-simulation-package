
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Dolphin(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 6 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of battle: Deal 5 damage to the lowest health enemy
    # lvl 2: Start of battle: Deal 10 damage to the lowest health enemy
    # lvl 3: Start of battle: Deal 15 damage to the lowest health enemy
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.DOLPHIN, tier = 4, ability=self.ability)

      