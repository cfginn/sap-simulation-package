
import unittest
from pysapets.cricket import Cricket
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class CricketTest(unittest.TestCase):

  def setUp(self):
    self.cricket = Cricket()
    self.friends = [self.cricket, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.cricket.get_type(), constants.CRICKET)

  # test that cricket starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.cricket.get_health(), 2)
  
  # test that cricket starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.cricket.get_attack(), 1)
  
  # test that initializing cricket with additional health increases health
  def test_init_add_health(self):
    newCricket = Cricket(addHealth = 3)
    self.assertEqual(newCricket.get_health(), 2 + 3)
  
  # test that initializing an cricket with additional attack increases attack
  def test_init_add_attack(self):
    newCricket = Cricket(addAttack = 3)
    self.assertEqual(newCricket.get_attack(), 1 + 3)
  
  # test that initializing cricket with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newCricket = Cricket(addHealth = 3, addAttack = 3)
    self.assertEqual(newCricket.get_health(), 2 + 3)
    self.assertEqual(newCricket.get_attack(), 1 + 3)
  
  # test that cricket ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.cricket.get_ability_trigger(), constants.FAINT)
  
  # test that cricket ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.cricket.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for cricket ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      