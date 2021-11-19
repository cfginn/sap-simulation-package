
import unittest
from pysapets.monkey import Monkey
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class MonkeyTest(unittest.TestCase):

  def setUp(self):
    self.monkey = Monkey()
    self.friends = [self.monkey, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.monkey.get_type(), constants.MONKEY)

  # test that monkey starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.monkey.get_health(), 3)
  
  # test that monkey starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.monkey.get_attack(), 3)
  
  # test that initializing monkey with additional health increases health
  def test_init_add_health(self):
    newMonkey = Monkey(addHealth = 3)
    self.assertEqual(newMonkey.get_health(), 3 + 3)
  
  # test that initializing an monkey with additional attack increases attack
  def test_init_add_attack(self):
    newMonkey = Monkey(addAttack = 3)
    self.assertEqual(newMonkey.get_attack(), 3 + 3)
  
  # test that initializing monkey with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newMonkey = Monkey(addHealth = 3, addAttack = 3)
    self.assertEqual(newMonkey.get_health(), 3 + 3)
    self.assertEqual(newMonkey.get_attack(), 3 + 3)
  
  # test that monkey ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.monkey.get_ability_trigger(), constants.END_OF_TURN)
  
  # test that monkey ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.monkey.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for monkey ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      