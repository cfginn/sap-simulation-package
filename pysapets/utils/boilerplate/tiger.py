
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Tiger(Animal):
  # base health and attack values
  BASE_ATTACK = 4 
  BASE_HEALTH = 3 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: The friend ahead casts their ability twice in battle.
    # lvl 2: The friend ahead casts their ability twice in battle.
    # lvl 3: The friend ahead casts their ability twice in battle.
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.CASTS_ABILITY, constants.FRIEND_AHEAD, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.TIGER, tier = 6, ability=self.ability)

      