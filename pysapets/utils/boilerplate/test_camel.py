
import unittest
from pysapets.camel import Camel
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class CamelTest(unittest.TestCase):

  def setUp(self):
    self.camel = Camel()
    self.friends = [self.camel, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.camel.get_type(), constants.CAMEL)

  # test that camel starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.camel.get_health(), 5)
  
  # test that camel starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.camel.get_attack(), 2)
  
  # test that initializing camel with additional health increases health
  def test_init_add_health(self):
    newCamel = Camel(addHealth = 3)
    self.assertEqual(newCamel.get_health(), 5 + 3)
  
  # test that initializing an camel with additional attack increases attack
  def test_init_add_attack(self):
    newCamel = Camel(addAttack = 3)
    self.assertEqual(newCamel.get_attack(), 2 + 3)
  
  # test that initializing camel with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newCamel = Camel(addHealth = 3, addAttack = 3)
    self.assertEqual(newCamel.get_health(), 5 + 3)
    self.assertEqual(newCamel.get_attack(), 2 + 3)
  
  # test that camel ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.camel.get_ability_trigger(), constants.HURT)
  
  # test that camel ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.camel.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for camel ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      