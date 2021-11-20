
from pysapets.animal import Animal
import pysapets.constants as constants
import random
import logging

class Ox(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend ahead attacks: Gain Melon Armor and +2 attack
    # lvl 2: Friend ahead attacks: Gain Melon Armor and +4 attack
    # lvl 3: Friend ahead attacks: Gain Melon Armor and +6 attack
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.FRIEND_AHEAD, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.OX, tier = 3, ability=self.ability)

      