
import unittest
from pysapets.dolphin import Dolphin
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class DolphinTest(unittest.TestCase):

  def setUp(self):
    self.dolphin = Dolphin()
    self.friends = [self.dolphin, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.dolphin.get_type(), constants.DOLPHIN)

  # test that dolphin starts with base health of 6
  def test_get_health(self):
    self.assertEqual(self.dolphin.get_health(), 6)
  
  # test that dolphin starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.dolphin.get_attack(), 4)
  
  # test that initializing dolphin with additional health increases health
  def test_init_add_health(self):
    newDolphin = Dolphin(addHealth = 3)
    self.assertEqual(newDolphin.get_health(), 6 + 3)
  
  # test that initializing an dolphin with additional attack increases attack
  def test_init_add_attack(self):
    newDolphin = Dolphin(addAttack = 3)
    self.assertEqual(newDolphin.get_attack(), 4 + 3)
  
  # test that initializing dolphin with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newDolphin = Dolphin(addHealth = 3, addAttack = 3)
    self.assertEqual(newDolphin.get_health(), 6 + 3)
    self.assertEqual(newDolphin.get_attack(), 4 + 3)
  
  # test that dolphin ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.dolphin.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that dolphin ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.dolphin.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for dolphin ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      