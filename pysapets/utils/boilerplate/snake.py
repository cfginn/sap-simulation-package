
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Snake(Animal):
  # base health and attack values
  BASE_ATTACK = 6 
  BASE_HEALTH = 6 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend ahead attacks: Deal 5 damage to a random enemy.
    # lvl 2: Friend ahead attacks: Deal 10 damage to a random enemy.
    # lvl 3: Friend ahead attacks: Deal 15 damage to a random enemy.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.AFTER_ATTACK, constants.FRIEND_AHEAD, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.SNAKE, tier = 6, ability=self.ability)

      