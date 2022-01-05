
import unittest
from pysapets.badger import Badger
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BadgerTest(unittest.TestCase):

  def setUp(self):
    self.badger = Badger()
    self.friends = [self.badger, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.badger.get_type(), constants.BADGER)

  # test that badger starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.badger.get_health(), 4)
  
  # test that badger starts with base attack of 5 
  def test_get_attack(self):
    self.assertEqual(self.badger.get_attack(), 5)
  
  # test that initializing badger with additional health increases health
  def test_init_add_health(self):
    newBadger = Badger(addHealth = 3)
    self.assertEqual(newBadger.get_health(), 4 + 3)
  
  # test that initializing an badger with additional attack increases attack
  def test_init_add_attack(self):
    newBadger = Badger(addAttack = 3)
    self.assertEqual(newBadger.get_attack(), 5 + 3)
  
  # test that initializing badger with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBadger = Badger(addHealth = 3, addAttack = 3)
    self.assertEqual(newBadger.get_health(), 4 + 3)
    self.assertEqual(newBadger.get_attack(), 5 + 3)
  
  # test that badger ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.badger.get_ability_trigger(), constants.EATS_SHOP_FOOD)
  
  # test that badger ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.badger.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for badger ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      