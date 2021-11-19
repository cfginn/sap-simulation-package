
import unittest
from pysapets.crocodile import Crocodile
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class CrocodileTest(unittest.TestCase):

  def setUp(self):
    self.crocodile = Crocodile()
    self.friends = [self.crocodile, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.crocodile.get_type(), constants.CROCODILE)

  # test that crocodile starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.crocodile.get_health(), 3)
  
  # test that crocodile starts with base attack of 6 
  def test_get_attack(self):
    self.assertEqual(self.crocodile.get_attack(), 6)
  
  # test that initializing crocodile with additional health increases health
  def test_init_add_health(self):
    newCrocodile = Crocodile(addHealth = 3)
    self.assertEqual(newCrocodile.get_health(), 3 + 3)
  
  # test that initializing an crocodile with additional attack increases attack
  def test_init_add_attack(self):
    newCrocodile = Crocodile(addAttack = 3)
    self.assertEqual(newCrocodile.get_attack(), 6 + 3)
  
  # test that initializing crocodile with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newCrocodile = Crocodile(addHealth = 3, addAttack = 3)
    self.assertEqual(newCrocodile.get_health(), 3 + 3)
    self.assertEqual(newCrocodile.get_attack(), 6 + 3)
  
  # test that crocodile ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.crocodile.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that crocodile ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.crocodile.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for crocodile ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      