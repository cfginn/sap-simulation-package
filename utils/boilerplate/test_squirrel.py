
import unittest
from pysapets.squirrel import Squirrel
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SquirrelTest(unittest.TestCase):

  def setUp(self):
    self.squirrel = Squirrel()
    self.friends = [self.squirrel, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.squirrel.get_type(), constants.SQUIRREL)

  # test that squirrel starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.squirrel.get_health(), 2)
  
  # test that squirrel starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.squirrel.get_attack(), 2)
  
  # test that initializing squirrel with additional health increases health
  def test_init_add_health(self):
    newSquirrel = Squirrel(addHealth = 3)
    self.assertEqual(newSquirrel.get_health(), 2 + 3)
  
  # test that initializing an squirrel with additional attack increases attack
  def test_init_add_attack(self):
    newSquirrel = Squirrel(addAttack = 3)
    self.assertEqual(newSquirrel.get_attack(), 2 + 3)
  
  # test that initializing squirrel with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSquirrel = Squirrel(addHealth = 3, addAttack = 3)
    self.assertEqual(newSquirrel.get_health(), 2 + 3)
    self.assertEqual(newSquirrel.get_attack(), 2 + 3)
  
  # test that squirrel ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.squirrel.get_ability_trigger(), constants.LEVEL_UP)
  
  # test that squirrel ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.squirrel.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for squirrel ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      