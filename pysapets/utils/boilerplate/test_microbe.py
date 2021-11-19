
import unittest
from pysapets.microbe import Microbe
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class MicrobeTest(unittest.TestCase):

  def setUp(self):
    self.microbe = Microbe()
    self.friends = [self.microbe, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.microbe.get_type(), constants.MICROBE)

  # test that microbe starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.microbe.get_health(), 1)
  
  # test that microbe starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.microbe.get_attack(), 1)
  
  # test that initializing microbe with additional health increases health
  def test_init_add_health(self):
    newMicrobe = Microbe(addHealth = 3)
    self.assertEqual(newMicrobe.get_health(), 1 + 3)
  
  # test that initializing an microbe with additional attack increases attack
  def test_init_add_attack(self):
    newMicrobe = Microbe(addAttack = 3)
    self.assertEqual(newMicrobe.get_attack(), 1 + 3)
  
  # test that initializing microbe with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newMicrobe = Microbe(addHealth = 3, addAttack = 3)
    self.assertEqual(newMicrobe.get_health(), 1 + 3)
    self.assertEqual(newMicrobe.get_attack(), 1 + 3)
  
  # test that microbe ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.microbe.get_ability_trigger(), constants.FAINT)
  
  # test that microbe ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.microbe.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for microbe ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      