
import unittest
from pysapets.beaver import Beaver
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BeaverTest(unittest.TestCase):

  def setUp(self):
    self.beaver = Beaver()
    self.friends = [self.beaver, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.beaver.get_type(), constants.BEAVER)

  # test that beaver starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.beaver.get_health(), 2)
  
  # test that beaver starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.beaver.get_attack(), 2)
  
  # test that initializing beaver with additional health increases health
  def test_init_add_health(self):
    newBeaver = Beaver(addHealth = 3)
    self.assertEqual(newBeaver.get_health(), 2 + 3)
  
  # test that initializing an beaver with additional attack increases attack
  def test_init_add_attack(self):
    newBeaver = Beaver(addAttack = 3)
    self.assertEqual(newBeaver.get_attack(), 2 + 3)
  
  # test that initializing beaver with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBeaver = Beaver(addHealth = 3, addAttack = 3)
    self.assertEqual(newBeaver.get_health(), 2 + 3)
    self.assertEqual(newBeaver.get_attack(), 2 + 3)
  
  # test that beaver ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.beaver.get_ability_trigger(), constants.SELL)
  
  # test that beaver ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.beaver.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for beaver ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      