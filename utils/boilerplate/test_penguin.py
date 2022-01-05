
import unittest
from pysapets.penguin import Penguin
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class PenguinTest(unittest.TestCase):

  def setUp(self):
    self.penguin = Penguin()
    self.friends = [self.penguin, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.penguin.get_type(), constants.PENGUIN)

  # test that penguin starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.penguin.get_health(), 2)
  
  # test that penguin starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.penguin.get_attack(), 1)
  
  # test that initializing penguin with additional health increases health
  def test_init_add_health(self):
    newPenguin = Penguin(addHealth = 3)
    self.assertEqual(newPenguin.get_health(), 2 + 3)
  
  # test that initializing an penguin with additional attack increases attack
  def test_init_add_attack(self):
    newPenguin = Penguin(addAttack = 3)
    self.assertEqual(newPenguin.get_attack(), 1 + 3)
  
  # test that initializing penguin with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newPenguin = Penguin(addHealth = 3, addAttack = 3)
    self.assertEqual(newPenguin.get_health(), 2 + 3)
    self.assertEqual(newPenguin.get_attack(), 1 + 3)
  
  # test that penguin ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.penguin.get_ability_trigger(), constants.END_OF_TURN)
  
  # test that penguin ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.penguin.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for penguin ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      