
import unittest
from pysapets.dodo import Dodo
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class DodoTest(unittest.TestCase):

  def setUp(self):
    self.dodo = Dodo()
    self.friends = [self.dodo, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.dodo.get_type(), constants.DODO)

  # test that dodo starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.dodo.get_health(), 3)
  
  # test that dodo starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.dodo.get_attack(), 1)
  
  # test that initializing dodo with additional health increases health
  def test_init_add_health(self):
    newDodo = Dodo(addHealth = 3)
    self.assertEqual(newDodo.get_health(), 3 + 3)
  
  # test that initializing an dodo with additional attack increases attack
  def test_init_add_attack(self):
    newDodo = Dodo(addAttack = 3)
    self.assertEqual(newDodo.get_attack(), 1 + 3)
  
  # test that initializing dodo with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newDodo = Dodo(addHealth = 3, addAttack = 3)
    self.assertEqual(newDodo.get_health(), 3 + 3)
    self.assertEqual(newDodo.get_attack(), 1 + 3)
  
  # test that dodo ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.dodo.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that dodo ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.dodo.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for dodo ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      