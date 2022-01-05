
import unittest
from pysapets.bat import Bat
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BatTest(unittest.TestCase):

  def setUp(self):
    self.bat = Bat()
    self.friends = [self.bat, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.bat.get_type(), constants.BAT)

  # test that bat starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.bat.get_health(), 2)
  
  # test that bat starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.bat.get_attack(), 1)
  
  # test that initializing bat with additional health increases health
  def test_init_add_health(self):
    newBat = Bat(addHealth = 3)
    self.assertEqual(newBat.get_health(), 2 + 3)
  
  # test that initializing an bat with additional attack increases attack
  def test_init_add_attack(self):
    newBat = Bat(addAttack = 3)
    self.assertEqual(newBat.get_attack(), 1 + 3)
  
  # test that initializing bat with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBat = Bat(addHealth = 3, addAttack = 3)
    self.assertEqual(newBat.get_health(), 2 + 3)
    self.assertEqual(newBat.get_attack(), 1 + 3)
  
  # test that bat ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.bat.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that bat ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.bat.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for bat ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      