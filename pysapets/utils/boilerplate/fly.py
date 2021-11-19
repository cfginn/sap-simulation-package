
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Fly(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Friend faints: Summon a 2/2 fly in its place
    # lvl 2: Friend faints: Summon a 4/4 fly in its place
    # lvl 3: Friend faints: Summon a 6/6 fly in its place
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.EACH_FRIEND, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.FLY, tier = 6, ability=self.ability)

      