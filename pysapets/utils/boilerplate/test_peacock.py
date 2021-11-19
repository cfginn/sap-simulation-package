
import unittest
from pysapets.peacock import Peacock
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class PeacockTest(unittest.TestCase):

  def setUp(self):
    self.peacock = Peacock()
    self.friends = [self.peacock, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.peacock.get_type(), constants.PEACOCK)

  # test that peacock starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.peacock.get_health(), 5)
  
  # test that peacock starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.peacock.get_attack(), 1)
  
  # test that initializing peacock with additional health increases health
  def test_init_add_health(self):
    newPeacock = Peacock(addHealth = 3)
    self.assertEqual(newPeacock.get_health(), 5 + 3)
  
  # test that initializing an peacock with additional attack increases attack
  def test_init_add_attack(self):
    newPeacock = Peacock(addAttack = 3)
    self.assertEqual(newPeacock.get_attack(), 1 + 3)
  
  # test that initializing peacock with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newPeacock = Peacock(addHealth = 3, addAttack = 3)
    self.assertEqual(newPeacock.get_health(), 5 + 3)
    self.assertEqual(newPeacock.get_attack(), 1 + 3)
  
  # test that peacock ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.peacock.get_ability_trigger(), constants.HURT)
  
  # test that peacock ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.peacock.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for peacock ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      