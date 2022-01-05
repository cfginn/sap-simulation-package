
import unittest
from pysapets.butterfly import Butterfly
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class ButterflyTest(unittest.TestCase):

  def setUp(self):
    self.butterfly = Butterfly()
    self.friends = [self.butterfly, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.butterfly.get_type(), constants.BUTTERFLY)

  # test that butterfly starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.butterfly.get_health(), 1)
  
  # test that butterfly starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.butterfly.get_attack(), 1)
  
  # test that initializing butterfly with additional health increases health
  def test_init_add_health(self):
    newButterfly = Butterfly(addHealth = 3)
    self.assertEqual(newButterfly.get_health(), 1 + 3)
  
  # test that initializing an butterfly with additional attack increases attack
  def test_init_add_attack(self):
    newButterfly = Butterfly(addAttack = 3)
    self.assertEqual(newButterfly.get_attack(), 1 + 3)
  
  # test that initializing butterfly with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newButterfly = Butterfly(addHealth = 3, addAttack = 3)
    self.assertEqual(newButterfly.get_health(), 1 + 3)
    self.assertEqual(newButterfly.get_attack(), 1 + 3)
  
  # test that butterfly ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.butterfly.get_ability_trigger(), constants.SUMMONED)
  
  # test that butterfly ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.butterfly.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for butterfly ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      