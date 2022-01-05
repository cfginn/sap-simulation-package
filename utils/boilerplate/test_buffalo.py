
import unittest
from pysapets.buffalo import Buffalo
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BuffaloTest(unittest.TestCase):

  def setUp(self):
    self.buffalo = Buffalo()
    self.friends = [self.buffalo, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.buffalo.get_type(), constants.BUFFALO)

  # test that buffalo starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.buffalo.get_health(), 5)
  
  # test that buffalo starts with base attack of 5 
  def test_get_attack(self):
    self.assertEqual(self.buffalo.get_attack(), 5)
  
  # test that initializing buffalo with additional health increases health
  def test_init_add_health(self):
    newBuffalo = Buffalo(addHealth = 3)
    self.assertEqual(newBuffalo.get_health(), 5 + 3)
  
  # test that initializing an buffalo with additional attack increases attack
  def test_init_add_attack(self):
    newBuffalo = Buffalo(addAttack = 3)
    self.assertEqual(newBuffalo.get_attack(), 5 + 3)
  
  # test that initializing buffalo with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBuffalo = Buffalo(addHealth = 3, addAttack = 3)
    self.assertEqual(newBuffalo.get_health(), 5 + 3)
    self.assertEqual(newBuffalo.get_attack(), 5 + 3)
  
  # test that buffalo ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.buffalo.get_ability_trigger(), constants.BUY)
  
  # test that buffalo ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.buffalo.get_ability_triggeredBy(), constants.EACH_FRIEND)
  
  # TODO add relevant tests for buffalo ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      