
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Crocodile(Animal):
  # base health and attack values
  BASE_ATTACK = 6 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of battle: Deal 7 damage to the last enemy
    # lvl 2: Start of battle: Deal 14 damage to the last enemy
    # lvl 3: Start of battle: Deal 21 damage to the last enemy
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.CROCODILE, tier = 5, ability=self.ability)

      