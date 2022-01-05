
import unittest
from pysapets.poodle import Poodle
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class PoodleTest(unittest.TestCase):

  def setUp(self):
    self.poodle = Poodle()
    self.friends = [self.poodle, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.poodle.get_type(), constants.POODLE)

  # test that poodle starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.poodle.get_health(), 2)
  
  # test that poodle starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.poodle.get_attack(), 4)
  
  # test that initializing poodle with additional health increases health
  def test_init_add_health(self):
    newPoodle = Poodle(addHealth = 3)
    self.assertEqual(newPoodle.get_health(), 2 + 3)
  
  # test that initializing an poodle with additional attack increases attack
  def test_init_add_attack(self):
    newPoodle = Poodle(addAttack = 3)
    self.assertEqual(newPoodle.get_attack(), 4 + 3)
  
  # test that initializing poodle with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newPoodle = Poodle(addHealth = 3, addAttack = 3)
    self.assertEqual(newPoodle.get_health(), 2 + 3)
    self.assertEqual(newPoodle.get_attack(), 4 + 3)
  
  # test that poodle ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.poodle.get_ability_trigger(), constants.END_OF_TURN)
  
  # test that poodle ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.poodle.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for poodle ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      