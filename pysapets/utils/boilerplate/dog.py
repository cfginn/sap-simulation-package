
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Dog(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend summoned: Gain +1 Attack or +1 Health.
    # lvl 2: Friend summoned: Gain +2 Attack or +2 Health.
    # lvl 3: Friend summoned: Gain +3 Attack or +3 Health.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.DOG, tier = 2, ability=self.ability)

      