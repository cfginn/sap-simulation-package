
from pysapets.animal import Animal
from pysapets.zombie_cricket import ZombieCricket
import pysapets.constants as constants
import random
import logging

class Cricket(Animal):
  # base health and attack values
  BASE_ATTACK = 1 
  BASE_HEALTH = 2 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: Faint: Summon a 1/1 Cricket
    # lvl 2: Faint: Summon a 2/2 Cricket
    # lvl 3: Faint: Summon a 3/3 Cricket
    def _run_effect(self, **kwargs):
      friends = kwargs['friends']
      # if cricket still alive do nothing
      if not self.dead:
        logging.error("{}: {}".format("Cricket", constants.ERROR_STILL_ALIVE))
        return

      if 'teamName' in kwargs:
        teamName = kwargs['teamName']
      else:
        teamName = "None"

      index_of_self = friends.index(self)

      zombieCricket = ZombieCricket(self)

      # replace cricket with zombie in friends in place
      friends[:] = [zombieCricket if friend == self else friend for friend in friends]

      print("{}-{}-{} has been replaced with a zombie cricket".format(teamName, index_of_self, self.get_type()))
 
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.CRICKET, tier = 1, ability=self.ability)

      