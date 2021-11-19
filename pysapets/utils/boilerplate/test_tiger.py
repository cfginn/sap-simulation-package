
import unittest
from pysapets.tiger import Tiger
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class TigerTest(unittest.TestCase):

  def setUp(self):
    self.tiger = Tiger()
    self.friends = [self.tiger, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.tiger.get_type(), constants.TIGER)

  # test that tiger starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.tiger.get_health(), 3)
  
  # test that tiger starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.tiger.get_attack(), 4)
  
  # test that initializing tiger with additional health increases health
  def test_init_add_health(self):
    newTiger = Tiger(addHealth = 3)
    self.assertEqual(newTiger.get_health(), 3 + 3)
  
  # test that initializing an tiger with additional attack increases attack
  def test_init_add_attack(self):
    newTiger = Tiger(addAttack = 3)
    self.assertEqual(newTiger.get_attack(), 4 + 3)
  
  # test that initializing tiger with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newTiger = Tiger(addHealth = 3, addAttack = 3)
    self.assertEqual(newTiger.get_health(), 3 + 3)
    self.assertEqual(newTiger.get_attack(), 4 + 3)
  
  # test that tiger ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.tiger.get_ability_trigger(), constants.CASTS_ABILITY)
  
  # test that tiger ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.tiger.get_ability_triggeredBy(), constants.FRIEND_AHEAD)
  
  # TODO add relevant tests for tiger ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      