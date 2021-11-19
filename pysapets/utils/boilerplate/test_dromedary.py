
import unittest
from pysapets.dromedary import Dromedary
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class DromedaryTest(unittest.TestCase):

  def setUp(self):
    self.dromedary = Dromedary()
    self.friends = [self.dromedary, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.dromedary.get_type(), constants.DROMEDARY)

  # test that dromedary starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.dromedary.get_health(), 4)
  
  # test that dromedary starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.dromedary.get_attack(), 2)
  
  # test that initializing dromedary with additional health increases health
  def test_init_add_health(self):
    newDromedary = Dromedary(addHealth = 3)
    self.assertEqual(newDromedary.get_health(), 4 + 3)
  
  # test that initializing an dromedary with additional attack increases attack
  def test_init_add_attack(self):
    newDromedary = Dromedary(addAttack = 3)
    self.assertEqual(newDromedary.get_attack(), 2 + 3)
  
  # test that initializing dromedary with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newDromedary = Dromedary(addHealth = 3, addAttack = 3)
    self.assertEqual(newDromedary.get_health(), 4 + 3)
    self.assertEqual(newDromedary.get_attack(), 2 + 3)
  
  # test that dromedary ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.dromedary.get_ability_trigger(), constants.START_OF_TURN)
  
  # test that dromedary ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.dromedary.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for dromedary ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      