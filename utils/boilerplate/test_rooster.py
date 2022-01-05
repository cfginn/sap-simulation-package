
import unittest
from pysapets.rooster import Rooster
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class RoosterTest(unittest.TestCase):

  def setUp(self):
    self.rooster = Rooster()
    self.friends = [self.rooster, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.rooster.get_type(), constants.ROOSTER)

  # test that rooster starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.rooster.get_health(), 3)
  
  # test that rooster starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.rooster.get_attack(), 3)
  
  # test that initializing rooster with additional health increases health
  def test_init_add_health(self):
    newRooster = Rooster(addHealth = 3)
    self.assertEqual(newRooster.get_health(), 3 + 3)
  
  # test that initializing an rooster with additional attack increases attack
  def test_init_add_attack(self):
    newRooster = Rooster(addAttack = 3)
    self.assertEqual(newRooster.get_attack(), 3 + 3)
  
  # test that initializing rooster with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newRooster = Rooster(addHealth = 3, addAttack = 3)
    self.assertEqual(newRooster.get_health(), 3 + 3)
    self.assertEqual(newRooster.get_attack(), 3 + 3)
  
  # test that rooster ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.rooster.get_ability_trigger(), constants.FAINT)
  
  # test that rooster ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.rooster.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for rooster ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      