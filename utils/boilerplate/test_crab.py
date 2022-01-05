
import unittest
from pysapets.crab import Crab
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class CrabTest(unittest.TestCase):

  def setUp(self):
    self.crab = Crab()
    self.friends = [self.crab, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.crab.get_type(), constants.CRAB)

  # test that crab starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.crab.get_health(), 3)
  
  # test that crab starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.crab.get_attack(), 3)
  
  # test that initializing crab with additional health increases health
  def test_init_add_health(self):
    newCrab = Crab(addHealth = 3)
    self.assertEqual(newCrab.get_health(), 3 + 3)
  
  # test that initializing an crab with additional attack increases attack
  def test_init_add_attack(self):
    newCrab = Crab(addAttack = 3)
    self.assertEqual(newCrab.get_attack(), 3 + 3)
  
  # test that initializing crab with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newCrab = Crab(addHealth = 3, addAttack = 3)
    self.assertEqual(newCrab.get_health(), 3 + 3)
    self.assertEqual(newCrab.get_attack(), 3 + 3)
  
  # test that crab ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.crab.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that crab ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.crab.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for crab ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      