
import unittest
from pysapets.cat import Cat
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class CatTest(unittest.TestCase):

  def setUp(self):
    self.cat = Cat()
    self.friends = [self.cat, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.cat.get_type(), constants.CAT)

  # test that cat starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.cat.get_health(), 5)
  
  # test that cat starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.cat.get_attack(), 4)
  
  # test that initializing cat with additional health increases health
  def test_init_add_health(self):
    newCat = Cat(addHealth = 3)
    self.assertEqual(newCat.get_health(), 5 + 3)
  
  # test that initializing an cat with additional attack increases attack
  def test_init_add_attack(self):
    newCat = Cat(addAttack = 3)
    self.assertEqual(newCat.get_attack(), 4 + 3)
  
  # test that initializing cat with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newCat = Cat(addHealth = 3, addAttack = 3)
    self.assertEqual(newCat.get_health(), 5 + 3)
    self.assertEqual(newCat.get_attack(), 4 + 3)
  
  # test that cat ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.cat.get_ability_trigger(), constants.HURT)
  
  # test that cat ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.cat.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for cat ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      