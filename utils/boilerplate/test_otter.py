
import unittest
from pysapets.otter import Otter
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class OtterTest(unittest.TestCase):

  def setUp(self):
    self.otter = Otter()
    self.friends = [self.otter, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.otter.get_type(), constants.OTTER)

  # test that otter starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.otter.get_health(), 2)
  
  # test that otter starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.otter.get_attack(), 1)
  
  # test that initializing otter with additional health increases health
  def test_init_add_health(self):
    newOtter = Otter(addHealth = 3)
    self.assertEqual(newOtter.get_health(), 2 + 3)
  
  # test that initializing an otter with additional attack increases attack
  def test_init_add_attack(self):
    newOtter = Otter(addAttack = 3)
    self.assertEqual(newOtter.get_attack(), 1 + 3)
  
  # test that initializing otter with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newOtter = Otter(addHealth = 3, addAttack = 3)
    self.assertEqual(newOtter.get_health(), 2 + 3)
    self.assertEqual(newOtter.get_attack(), 1 + 3)
  
  # test that otter ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.otter.get_ability_trigger(), constants.BUY)
  
  # test that otter ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.otter.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for otter ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      