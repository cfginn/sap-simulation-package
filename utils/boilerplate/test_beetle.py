
import unittest
from pysapets.beetle import Beetle
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BeetleTest(unittest.TestCase):

  def setUp(self):
    self.beetle = Beetle()
    self.friends = [self.beetle, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.beetle.get_type(), constants.BEETLE)

  # test that beetle starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.beetle.get_health(), 3)
  
  # test that beetle starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.beetle.get_attack(), 2)
  
  # test that initializing beetle with additional health increases health
  def test_init_add_health(self):
    newBeetle = Beetle(addHealth = 3)
    self.assertEqual(newBeetle.get_health(), 3 + 3)
  
  # test that initializing an beetle with additional attack increases attack
  def test_init_add_attack(self):
    newBeetle = Beetle(addAttack = 3)
    self.assertEqual(newBeetle.get_attack(), 2 + 3)
  
  # test that initializing beetle with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBeetle = Beetle(addHealth = 3, addAttack = 3)
    self.assertEqual(newBeetle.get_health(), 3 + 3)
    self.assertEqual(newBeetle.get_attack(), 2 + 3)
  
  # test that beetle ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.beetle.get_ability_trigger(), constants.EATS_SHOP_FOOD)
  
  # test that beetle ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.beetle.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for beetle ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      