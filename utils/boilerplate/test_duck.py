
import unittest
from pysapets.duck import Duck
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class DuckTest(unittest.TestCase):

  def setUp(self):
    self.duck = Duck()
    self.friends = [self.duck, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.duck.get_type(), constants.DUCK)

  # test that duck starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.duck.get_health(), 2)
  
  # test that duck starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.duck.get_attack(), 1)
  
  # test that initializing duck with additional health increases health
  def test_init_add_health(self):
    newDuck = Duck(addHealth = 3)
    self.assertEqual(newDuck.get_health(), 2 + 3)
  
  # test that initializing an duck with additional attack increases attack
  def test_init_add_attack(self):
    newDuck = Duck(addAttack = 3)
    self.assertEqual(newDuck.get_attack(), 1 + 3)
  
  # test that initializing duck with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newDuck = Duck(addHealth = 3, addAttack = 3)
    self.assertEqual(newDuck.get_health(), 2 + 3)
    self.assertEqual(newDuck.get_attack(), 1 + 3)
  
  # test that duck ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.duck.get_ability_trigger(), constants.SELL)
  
  # test that duck ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.duck.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for duck ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      