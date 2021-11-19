
import unittest
from pysapets.skunk import Skunk
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SkunkTest(unittest.TestCase):

  def setUp(self):
    self.skunk = Skunk()
    self.friends = [self.skunk, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.skunk.get_type(), constants.SKUNK)

  # test that skunk starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.skunk.get_health(), 5)
  
  # test that skunk starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.skunk.get_attack(), 3)
  
  # test that initializing skunk with additional health increases health
  def test_init_add_health(self):
    newSkunk = Skunk(addHealth = 3)
    self.assertEqual(newSkunk.get_health(), 5 + 3)
  
  # test that initializing an skunk with additional attack increases attack
  def test_init_add_attack(self):
    newSkunk = Skunk(addAttack = 3)
    self.assertEqual(newSkunk.get_attack(), 3 + 3)
  
  # test that initializing skunk with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSkunk = Skunk(addHealth = 3, addAttack = 3)
    self.assertEqual(newSkunk.get_health(), 5 + 3)
    self.assertEqual(newSkunk.get_attack(), 3 + 3)
  
  # test that skunk ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.skunk.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that skunk ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.skunk.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for skunk ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      