
import unittest
from pysapets.rat import Rat
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class RatTest(unittest.TestCase):

  def setUp(self):
    self.rat = Rat()
    self.friends = [self.rat, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.rat.get_type(), constants.RAT)

  # test that rat starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.rat.get_health(), 5)
  
  # test that rat starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.rat.get_attack(), 4)
  
  # test that initializing rat with additional health increases health
  def test_init_add_health(self):
    newRat = Rat(addHealth = 3)
    self.assertEqual(newRat.get_health(), 5 + 3)
  
  # test that initializing an rat with additional attack increases attack
  def test_init_add_attack(self):
    newRat = Rat(addAttack = 3)
    self.assertEqual(newRat.get_attack(), 4 + 3)
  
  # test that initializing rat with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newRat = Rat(addHealth = 3, addAttack = 3)
    self.assertEqual(newRat.get_health(), 5 + 3)
    self.assertEqual(newRat.get_attack(), 4 + 3)
  
  # test that rat ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.rat.get_ability_trigger(), constants.FAINT)
  
  # test that rat ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.rat.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for rat ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      