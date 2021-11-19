
import unittest
from pysapets.chick import Chick
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class ChickTest(unittest.TestCase):

  def setUp(self):
    self.chick = Chick()
    self.friends = [self.chick, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.chick.get_type(), constants.CHICK)

  # test that chick starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.chick.get_health(), 1)
  
  # test that chick starts with base attack of ? 
  def test_get_attack(self):
    self.assertEqual(self.chick.get_attack(), ?)
  
  # test that initializing chick with additional health increases health
  def test_init_add_health(self):
    newChick = Chick(addHealth = 3)
    self.assertEqual(newChick.get_health(), 1 + 3)
  
  # test that initializing an chick with additional attack increases attack
  def test_init_add_attack(self):
    newChick = Chick(addAttack = 3)
    self.assertEqual(newChick.get_attack(), ? + 3)
  
  # test that initializing chick with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newChick = Chick(addHealth = 3, addAttack = 3)
    self.assertEqual(newChick.get_health(), 1 + 3)
    self.assertEqual(newChick.get_attack(), ? + 3)
  
  # test that chick ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.chick.get_ability_trigger(), constants.END_OF_TURN_WITH_3_PLUS_GOLD)
  
  # test that chick ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.chick.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for chick ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      