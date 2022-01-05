
import unittest
from pysapets.goat import Goat
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class GoatTest(unittest.TestCase):

  def setUp(self):
    self.goat = Goat()
    self.friends = [self.goat, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.goat.get_type(), constants.GOAT)

  # test that goat starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.goat.get_health(), 5)
  
  # test that goat starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.goat.get_attack(), 4)
  
  # test that initializing goat with additional health increases health
  def test_init_add_health(self):
    newGoat = Goat(addHealth = 3)
    self.assertEqual(newGoat.get_health(), 5 + 3)
  
  # test that initializing an goat with additional attack increases attack
  def test_init_add_attack(self):
    newGoat = Goat(addAttack = 3)
    self.assertEqual(newGoat.get_attack(), 4 + 3)
  
  # test that initializing goat with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newGoat = Goat(addHealth = 3, addAttack = 3)
    self.assertEqual(newGoat.get_health(), 5 + 3)
    self.assertEqual(newGoat.get_attack(), 4 + 3)
  
  # test that goat ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.goat.get_ability_trigger(), constants.BUY)
  
  # test that goat ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.goat.get_ability_triggeredBy(), constants.EACH_FRIEND)
  
  # TODO add relevant tests for goat ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      