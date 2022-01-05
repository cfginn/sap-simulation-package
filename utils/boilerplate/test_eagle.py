
import unittest
from pysapets.eagle import Eagle
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class EagleTest(unittest.TestCase):

  def setUp(self):
    self.eagle = Eagle()
    self.friends = [self.eagle, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.eagle.get_type(), constants.EAGLE)

  # test that eagle starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.eagle.get_health(), 5)
  
  # test that eagle starts with base attack of 6 
  def test_get_attack(self):
    self.assertEqual(self.eagle.get_attack(), 6)
  
  # test that initializing eagle with additional health increases health
  def test_init_add_health(self):
    newEagle = Eagle(addHealth = 3)
    self.assertEqual(newEagle.get_health(), 5 + 3)
  
  # test that initializing an eagle with additional attack increases attack
  def test_init_add_attack(self):
    newEagle = Eagle(addAttack = 3)
    self.assertEqual(newEagle.get_attack(), 6 + 3)
  
  # test that initializing eagle with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newEagle = Eagle(addHealth = 3, addAttack = 3)
    self.assertEqual(newEagle.get_health(), 5 + 3)
    self.assertEqual(newEagle.get_attack(), 6 + 3)
  
  # test that eagle ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.eagle.get_ability_trigger(), constants.FAINT)
  
  # test that eagle ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.eagle.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for eagle ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      