
import unittest
from pysapets.pig import Pig
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class PigTest(unittest.TestCase):

  def setUp(self):
    self.pig = Pig()
    self.friends = [self.pig, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.pig.get_type(), constants.PIG)

  # test that pig starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.pig.get_health(), 2)
  
  # test that pig starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.pig.get_attack(), 2)
  
  # test that initializing pig with additional health increases health
  def test_init_add_health(self):
    newPig = Pig(addHealth = 3)
    self.assertEqual(newPig.get_health(), 2 + 3)
  
  # test that initializing an pig with additional attack increases attack
  def test_init_add_attack(self):
    newPig = Pig(addAttack = 3)
    self.assertEqual(newPig.get_attack(), 2 + 3)
  
  # test that initializing pig with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newPig = Pig(addHealth = 3, addAttack = 3)
    self.assertEqual(newPig.get_health(), 2 + 3)
    self.assertEqual(newPig.get_attack(), 2 + 3)
  
  # test that pig ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.pig.get_ability_trigger(), constants.SELL)
  
  # test that pig ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.pig.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for pig ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      