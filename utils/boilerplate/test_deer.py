
import unittest
from pysapets.deer import Deer
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class DeerTest(unittest.TestCase):

  def setUp(self):
    self.deer = Deer()
    self.friends = [self.deer, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.deer.get_type(), constants.DEER)

  # test that deer starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.deer.get_health(), 1)
  
  # test that deer starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.deer.get_attack(), 1)
  
  # test that initializing deer with additional health increases health
  def test_init_add_health(self):
    newDeer = Deer(addHealth = 3)
    self.assertEqual(newDeer.get_health(), 1 + 3)
  
  # test that initializing an deer with additional attack increases attack
  def test_init_add_attack(self):
    newDeer = Deer(addAttack = 3)
    self.assertEqual(newDeer.get_attack(), 1 + 3)
  
  # test that initializing deer with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newDeer = Deer(addHealth = 3, addAttack = 3)
    self.assertEqual(newDeer.get_health(), 1 + 3)
    self.assertEqual(newDeer.get_attack(), 1 + 3)
  
  # test that deer ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.deer.get_ability_trigger(), constants.FAINT)
  
  # test that deer ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.deer.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for deer ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      