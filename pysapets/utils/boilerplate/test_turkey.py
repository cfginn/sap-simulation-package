
import unittest
from pysapets.turkey import Turkey
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class TurkeyTest(unittest.TestCase):

  def setUp(self):
    self.turkey = Turkey()
    self.friends = [self.turkey, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.turkey.get_type(), constants.TURKEY)

  # test that turkey starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.turkey.get_health(), 4)
  
  # test that turkey starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.turkey.get_attack(), 3)
  
  # test that initializing turkey with additional health increases health
  def test_init_add_health(self):
    newTurkey = Turkey(addHealth = 3)
    self.assertEqual(newTurkey.get_health(), 4 + 3)
  
  # test that initializing an turkey with additional attack increases attack
  def test_init_add_attack(self):
    newTurkey = Turkey(addAttack = 3)
    self.assertEqual(newTurkey.get_attack(), 3 + 3)
  
  # test that initializing turkey with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newTurkey = Turkey(addHealth = 3, addAttack = 3)
    self.assertEqual(newTurkey.get_health(), 4 + 3)
    self.assertEqual(newTurkey.get_attack(), 3 + 3)
  
  # test that turkey ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.turkey.get_ability_trigger(), constants.SUMMONED)
  
  # test that turkey ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.turkey.get_ability_triggeredBy(), constants.EACH_FRIEND)
  
  # TODO add relevant tests for turkey ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      