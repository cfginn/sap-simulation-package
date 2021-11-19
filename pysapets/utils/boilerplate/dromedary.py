
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class Dromedary(Animal):
  # base health and attack values
  BASE_ATTACK = 2 
  BASE_HEALTH = 4 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Start of turn: Give shop animals +1/+1
    # lvl 2: Start of turn: Give shop animals +2/+2
    # lvl 3: Start of turn: Give shop animals +3/+3
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.START_OF_TURN, constants.PLAYER, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.DROMEDARY, tier = 2, ability=self.ability)

      