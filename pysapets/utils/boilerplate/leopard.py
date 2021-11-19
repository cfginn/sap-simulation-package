
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Leopard(Animal):
  # base health and attack values
  BASE_ATTACK = 6 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of battle: Deal 50% Attack damage to a random enemy.
    # lvl 2: Start of battle: Deal 50% Attack damage to 2 random enemies.
    # lvl 3: Start of battle: Deal 50% Attack damage to 3 random enemies.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.LEOPARD, tier = 6, ability=self.ability)

      