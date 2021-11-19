
import unittest
from pysapets.snail import Snail
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SnailTest(unittest.TestCase):

  def setUp(self):
    self.snail = Snail()
    self.friends = [self.snail, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.snail.get_type(), constants.SNAIL)

  # test that snail starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.snail.get_health(), 2)
  
  # test that snail starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.snail.get_attack(), 2)
  
  # test that initializing snail with additional health increases health
  def test_init_add_health(self):
    newSnail = Snail(addHealth = 3)
    self.assertEqual(newSnail.get_health(), 2 + 3)
  
  # test that initializing an snail with additional attack increases attack
  def test_init_add_attack(self):
    newSnail = Snail(addAttack = 3)
    self.assertEqual(newSnail.get_attack(), 2 + 3)
  
  # test that initializing snail with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSnail = Snail(addHealth = 3, addAttack = 3)
    self.assertEqual(newSnail.get_health(), 2 + 3)
    self.assertEqual(newSnail.get_attack(), 2 + 3)
  
  # test that snail ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.snail.get_ability_trigger(), constants.BUY_AFTER_LOSS)
  
  # test that snail ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.snail.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for snail ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      