
import unittest
from pysapets.mammoth import Mammoth
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class MammothTest(unittest.TestCase):

  def setUp(self):
    self.mammoth = Mammoth()
    self.friends = [self.mammoth, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.mammoth.get_type(), constants.MAMMOTH)

  # test that mammoth starts with base health of 6
  def test_get_health(self):
    self.assertEqual(self.mammoth.get_health(), 6)
  
  # test that mammoth starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.mammoth.get_attack(), 2)
  
  # test that initializing mammoth with additional health increases health
  def test_init_add_health(self):
    newMammoth = Mammoth(addHealth = 3)
    self.assertEqual(newMammoth.get_health(), 6 + 3)
  
  # test that initializing an mammoth with additional attack increases attack
  def test_init_add_attack(self):
    newMammoth = Mammoth(addAttack = 3)
    self.assertEqual(newMammoth.get_attack(), 2 + 3)
  
  # test that initializing mammoth with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newMammoth = Mammoth(addHealth = 3, addAttack = 3)
    self.assertEqual(newMammoth.get_health(), 6 + 3)
    self.assertEqual(newMammoth.get_attack(), 2 + 3)
  
  # test that mammoth ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.mammoth.get_ability_trigger(), constants.FAINT)
  
  # test that mammoth ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.mammoth.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for mammoth ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      