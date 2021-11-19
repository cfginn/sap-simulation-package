
import unittest
from pysapets.sloth import Sloth
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SlothTest(unittest.TestCase):

  def setUp(self):
    self.sloth = Sloth()
    self.friends = [self.sloth, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.sloth.get_type(), constants.SLOTH)

  # test that sloth starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.sloth.get_health(), 1)
  
  # test that sloth starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.sloth.get_attack(), 1)
  
  # test that initializing sloth with additional health increases health
  def test_init_add_health(self):
    newSloth = Sloth(addHealth = 3)
    self.assertEqual(newSloth.get_health(), 1 + 3)
  
  # test that initializing an sloth with additional attack increases attack
  def test_init_add_attack(self):
    newSloth = Sloth(addAttack = 3)
    self.assertEqual(newSloth.get_attack(), 1 + 3)
  
  # test that initializing sloth with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSloth = Sloth(addHealth = 3, addAttack = 3)
    self.assertEqual(newSloth.get_health(), 1 + 3)
    self.assertEqual(newSloth.get_attack(), 1 + 3)
  
  # test that sloth ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.sloth.get_ability_trigger(), constants.SELL)
  
  # test that sloth ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.sloth.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for sloth ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      