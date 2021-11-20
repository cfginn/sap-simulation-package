
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Blowfish(Animal):
  # base health and attack values
  BASE_ATTACK = 3 
  BASE_HEALTH = 5 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Hurt: Deal 2 damage to a random enemy.
    # lvl 2: Hurt: Deal 4 damage to a random enemy.
    # lvl 3: Hurt: Deal 6 damage to a random enemy.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.HURT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.BLOWFISH, tier = 3, ability=self.ability)

      