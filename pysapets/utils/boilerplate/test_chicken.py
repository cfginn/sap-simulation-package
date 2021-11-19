
import unittest
from pysapets.chicken import Chicken
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class ChickenTest(unittest.TestCase):

  def setUp(self):
    self.chicken = Chicken()
    self.friends = [self.chicken, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.chicken.get_type(), constants.CHICKEN)

  # test that chicken starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.chicken.get_health(), 4)
  
  # test that chicken starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.chicken.get_attack(), 3)
  
  # test that initializing chicken with additional health increases health
  def test_init_add_health(self):
    newChicken = Chicken(addHealth = 3)
    self.assertEqual(newChicken.get_health(), 4 + 3)
  
  # test that initializing an chicken with additional attack increases attack
  def test_init_add_attack(self):
    newChicken = Chicken(addAttack = 3)
    self.assertEqual(newChicken.get_attack(), 3 + 3)
  
  # test that initializing chicken with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newChicken = Chicken(addHealth = 3, addAttack = 3)
    self.assertEqual(newChicken.get_health(), 4 + 3)
    self.assertEqual(newChicken.get_attack(), 3 + 3)
  
  # test that chicken ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.chicken.get_ability_trigger(), constants.BUY_TIER_1_ANIMAL)
  
  # test that chicken ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.chicken.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for chicken ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      