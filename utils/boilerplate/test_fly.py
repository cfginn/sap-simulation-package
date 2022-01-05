
import unittest
from pysapets.fly import Fly
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class FlyTest(unittest.TestCase):

  def setUp(self):
    self.fly = Fly()
    self.friends = [self.fly, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.fly.get_type(), constants.FLY)

  # test that fly starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.fly.get_health(), 2)
  
  # test that fly starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.fly.get_attack(), 2)
  
  # test that initializing fly with additional health increases health
  def test_init_add_health(self):
    newFly = Fly(addHealth = 3)
    self.assertEqual(newFly.get_health(), 2 + 3)
  
  # test that initializing an fly with additional attack increases attack
  def test_init_add_attack(self):
    newFly = Fly(addAttack = 3)
    self.assertEqual(newFly.get_attack(), 2 + 3)
  
  # test that initializing fly with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newFly = Fly(addHealth = 3, addAttack = 3)
    self.assertEqual(newFly.get_health(), 2 + 3)
    self.assertEqual(newFly.get_attack(), 2 + 3)
  
  # test that fly ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.fly.get_ability_trigger(), constants.FAINT)
  
  # test that fly ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.fly.get_ability_triggeredBy(), constants.EACH_FRIEND)
  
  # TODO add relevant tests for fly ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      