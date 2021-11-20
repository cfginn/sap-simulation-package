
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Caterpillar(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of turn: Gain 1 Experience.
    # lvl 2: Start of turn: Gain 1 Experience.
    # lvl 3: Start of battle: Evolve into a Butterfly, then copy stats of the strongest friend.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.CATERPILLAR, tier = 3, ability=self.ability)

      