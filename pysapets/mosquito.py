
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Mosquito(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of battle: Deal 1 damage to a random enemy
    # lvl 2: Start of battle: Deal 2 damage to a random enemy
    # lvl 3: Start of battle: Deal 3 damage to a random enemy
    def _run_effect(self, **kwargs):
      enemies = kwargs['enemies']
      # choose a random enemy
      chosen_enemies = random.sample(enemies, k = self.level)
      # deal damage to the enemy
      for enemy in chosen_enemies:
        enemy.subtract_health(1) 
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_BATTLE, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.MOSQUITO, tier = 1, ability=self.ability)

      