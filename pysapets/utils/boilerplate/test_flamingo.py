
import unittest
from pysapets.flamingo import Flamingo
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class FlamingoTest(unittest.TestCase):

  def setUp(self):
    self.flamingo = Flamingo()
    self.friends = [self.flamingo, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.flamingo.get_type(), constants.FLAMINGO)

  # test that flamingo starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.flamingo.get_health(), 1)
  
  # test that flamingo starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.flamingo.get_attack(), 3)
  
  # test that initializing flamingo with additional health increases health
  def test_init_add_health(self):
    newFlamingo = Flamingo(addHealth = 3)
    self.assertEqual(newFlamingo.get_health(), 1 + 3)
  
  # test that initializing an flamingo with additional attack increases attack
  def test_init_add_attack(self):
    newFlamingo = Flamingo(addAttack = 3)
    self.assertEqual(newFlamingo.get_attack(), 3 + 3)
  
  # test that initializing flamingo with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newFlamingo = Flamingo(addHealth = 3, addAttack = 3)
    self.assertEqual(newFlamingo.get_health(), 1 + 3)
    self.assertEqual(newFlamingo.get_attack(), 3 + 3)
  
  # test that flamingo ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.flamingo.get_ability_trigger(), constants.FAINT)
  
  # test that flamingo ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.flamingo.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for flamingo ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      