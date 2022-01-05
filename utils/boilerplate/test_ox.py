
import unittest
from pysapets.ox import Ox
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class OxTest(unittest.TestCase):

  def setUp(self):
    self.ox = Ox()
    self.friends = [self.ox, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.ox.get_type(), constants.OX)

  # test that ox starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.ox.get_health(), 4)
  
  # test that ox starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.ox.get_attack(), 1)
  
  # test that initializing ox with additional health increases health
  def test_init_add_health(self):
    newOx = Ox(addHealth = 3)
    self.assertEqual(newOx.get_health(), 4 + 3)
  
  # test that initializing an ox with additional attack increases attack
  def test_init_add_attack(self):
    newOx = Ox(addAttack = 3)
    self.assertEqual(newOx.get_attack(), 1 + 3)
  
  # test that initializing ox with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newOx = Ox(addHealth = 3, addAttack = 3)
    self.assertEqual(newOx.get_health(), 4 + 3)
    self.assertEqual(newOx.get_attack(), 1 + 3)
  
  # test that ox ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.ox.get_ability_trigger(), constants.FAINT)
  
  # test that ox ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.ox.get_ability_triggeredBy(), constants.FRIEND_AHEAD)
  
  # TODO add relevant tests for ox ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      