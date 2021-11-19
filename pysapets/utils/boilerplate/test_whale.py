
import unittest
from pysapets.whale import Whale
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class WhaleTest(unittest.TestCase):

  def setUp(self):
    self.whale = Whale()
    self.friends = [self.whale, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.whale.get_type(), constants.WHALE)

  # test that whale starts with base health of 6
  def test_get_health(self):
    self.assertEqual(self.whale.get_health(), 6)
  
  # test that whale starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.whale.get_attack(), 2)
  
  # test that initializing whale with additional health increases health
  def test_init_add_health(self):
    newWhale = Whale(addHealth = 3)
    self.assertEqual(newWhale.get_health(), 6 + 3)
  
  # test that initializing an whale with additional attack increases attack
  def test_init_add_attack(self):
    newWhale = Whale(addAttack = 3)
    self.assertEqual(newWhale.get_attack(), 2 + 3)
  
  # test that initializing whale with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newWhale = Whale(addHealth = 3, addAttack = 3)
    self.assertEqual(newWhale.get_health(), 6 + 3)
    self.assertEqual(newWhale.get_attack(), 2 + 3)
  
  # test that whale ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.whale.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that whale ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.whale.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for whale ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      