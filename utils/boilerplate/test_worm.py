
import unittest
from pysapets.worm import Worm
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class WormTest(unittest.TestCase):

  def setUp(self):
    self.worm = Worm()
    self.friends = [self.worm, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.worm.get_type(), constants.WORM)

  # test that worm starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.worm.get_health(), 1)
  
  # test that worm starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.worm.get_attack(), 1)
  
  # test that initializing worm with additional health increases health
  def test_init_add_health(self):
    newWorm = Worm(addHealth = 3)
    self.assertEqual(newWorm.get_health(), 1 + 3)
  
  # test that initializing an worm with additional attack increases attack
  def test_init_add_attack(self):
    newWorm = Worm(addAttack = 3)
    self.assertEqual(newWorm.get_attack(), 1 + 3)
  
  # test that initializing worm with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newWorm = Worm(addHealth = 3, addAttack = 3)
    self.assertEqual(newWorm.get_health(), 1 + 3)
    self.assertEqual(newWorm.get_attack(), 1 + 3)
  
  # test that worm ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.worm.get_ability_trigger(), constants.EATS_SHOP_FOOD)
  
  # test that worm ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.worm.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for worm ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      