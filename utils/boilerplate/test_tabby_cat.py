
import unittest
from pysapets.tabby_cat import Tabby_cat
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class Tabby_catTest(unittest.TestCase):

  def setUp(self):
    self.tabby_cat = Tabby_cat()
    self.friends = [self.tabby_cat, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.tabby_cat.get_type(), constants.TABBY_CAT)

  # test that tabby_cat starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.tabby_cat.get_health(), 3)
  
  # test that tabby_cat starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.tabby_cat.get_attack(), 4)
  
  # test that initializing tabby_cat with additional health increases health
  def test_init_add_health(self):
    newTabby_cat = Tabby_cat(addHealth = 3)
    self.assertEqual(newTabby_cat.get_health(), 3 + 3)
  
  # test that initializing an tabby_cat with additional attack increases attack
  def test_init_add_attack(self):
    newTabby_cat = Tabby_cat(addAttack = 3)
    self.assertEqual(newTabby_cat.get_attack(), 4 + 3)
  
  # test that initializing tabby_cat with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newTabby_cat = Tabby_cat(addHealth = 3, addAttack = 3)
    self.assertEqual(newTabby_cat.get_health(), 3 + 3)
    self.assertEqual(newTabby_cat.get_attack(), 4 + 3)
  
  # test that tabby_cat ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.tabby_cat.get_ability_trigger(), constants.EATS_SHOP_FOOD)
  
  # test that tabby_cat ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.tabby_cat.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for tabby_cat ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      