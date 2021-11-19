
import unittest
from pysapets.cow import Cow
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class CowTest(unittest.TestCase):

  def setUp(self):
    self.cow = Cow()
    self.friends = [self.cow, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.cow.get_type(), constants.COW)

  # test that cow starts with base health of 6
  def test_get_health(self):
    self.assertEqual(self.cow.get_health(), 6)
  
  # test that cow starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.cow.get_attack(), 4)
  
  # test that initializing cow with additional health increases health
  def test_init_add_health(self):
    newCow = Cow(addHealth = 3)
    self.assertEqual(newCow.get_health(), 6 + 3)
  
  # test that initializing an cow with additional attack increases attack
  def test_init_add_attack(self):
    newCow = Cow(addAttack = 3)
    self.assertEqual(newCow.get_attack(), 4 + 3)
  
  # test that initializing cow with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newCow = Cow(addHealth = 3, addAttack = 3)
    self.assertEqual(newCow.get_health(), 6 + 3)
    self.assertEqual(newCow.get_attack(), 4 + 3)
  
  # test that cow ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.cow.get_ability_trigger(), constants.BUY)
  
  # test that cow ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.cow.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for cow ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      