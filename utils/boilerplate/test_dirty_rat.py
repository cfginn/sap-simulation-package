
import unittest
from pysapets.dirty_rat import Dirty_rat
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class Dirty_ratTest(unittest.TestCase):

  def setUp(self):
    self.dirty_rat = Dirty_rat()
    self.friends = [self.dirty_rat, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.dirty_rat.get_type(), constants.DIRTY_RAT)

  # test that dirty_rat starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.dirty_rat.get_health(), 1)
  
  # test that dirty_rat starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.dirty_rat.get_attack(), 1)
  
  # test that initializing dirty_rat with additional health increases health
  def test_init_add_health(self):
    newDirty_rat = Dirty_rat(addHealth = 3)
    self.assertEqual(newDirty_rat.get_health(), 1 + 3)
  
  # test that initializing an dirty_rat with additional attack increases attack
  def test_init_add_attack(self):
    newDirty_rat = Dirty_rat(addAttack = 3)
    self.assertEqual(newDirty_rat.get_attack(), 1 + 3)
  
  # test that initializing dirty_rat with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newDirty_rat = Dirty_rat(addHealth = 3, addAttack = 3)
    self.assertEqual(newDirty_rat.get_health(), 1 + 3)
    self.assertEqual(newDirty_rat.get_attack(), 1 + 3)
  
  # test that dirty_rat ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.dirty_rat.get_ability_trigger(), constants.END_OF_TURN_WITH_3_PLUS_GOLD)
  
  # test that dirty_rat ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.dirty_rat.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for dirty_rat ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      