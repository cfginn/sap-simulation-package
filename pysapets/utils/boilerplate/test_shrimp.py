
import unittest
from pysapets.shrimp import Shrimp
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class ShrimpTest(unittest.TestCase):

  def setUp(self):
    self.shrimp = Shrimp()
    self.friends = [self.shrimp, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.shrimp.get_type(), constants.SHRIMP)

  # test that shrimp starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.shrimp.get_health(), 1)
  
  # test that shrimp starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.shrimp.get_attack(), 2)
  
  # test that initializing shrimp with additional health increases health
  def test_init_add_health(self):
    newShrimp = Shrimp(addHealth = 3)
    self.assertEqual(newShrimp.get_health(), 1 + 3)
  
  # test that initializing an shrimp with additional attack increases attack
  def test_init_add_attack(self):
    newShrimp = Shrimp(addAttack = 3)
    self.assertEqual(newShrimp.get_attack(), 2 + 3)
  
  # test that initializing shrimp with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newShrimp = Shrimp(addHealth = 3, addAttack = 3)
    self.assertEqual(newShrimp.get_health(), 1 + 3)
    self.assertEqual(newShrimp.get_attack(), 2 + 3)
  
  # test that shrimp ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.shrimp.get_ability_trigger(), constants.SELL)
  
  # test that shrimp ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.shrimp.get_ability_triggeredBy(), constants.EACH_FRIEND)
  
  # TODO add relevant tests for shrimp ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      