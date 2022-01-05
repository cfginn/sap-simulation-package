
import unittest
from pysapets.rhino import Rhino
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class RhinoTest(unittest.TestCase):

  def setUp(self):
    self.rhino = Rhino()
    self.friends = [self.rhino, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.rhino.get_type(), constants.RHINO)

  # test that rhino starts with base health of 6
  def test_get_health(self):
    self.assertEqual(self.rhino.get_health(), 6)
  
  # test that rhino starts with base attack of 5 
  def test_get_attack(self):
    self.assertEqual(self.rhino.get_attack(), 5)
  
  # test that initializing rhino with additional health increases health
  def test_init_add_health(self):
    newRhino = Rhino(addHealth = 3)
    self.assertEqual(newRhino.get_health(), 6 + 3)
  
  # test that initializing an rhino with additional attack increases attack
  def test_init_add_attack(self):
    newRhino = Rhino(addAttack = 3)
    self.assertEqual(newRhino.get_attack(), 5 + 3)
  
  # test that initializing rhino with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newRhino = Rhino(addHealth = 3, addAttack = 3)
    self.assertEqual(newRhino.get_health(), 6 + 3)
    self.assertEqual(newRhino.get_attack(), 5 + 3)
  
  # test that rhino ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.rhino.get_ability_trigger(), constants.KNOCK_OUT)
  
  # test that rhino ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.rhino.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for rhino ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      