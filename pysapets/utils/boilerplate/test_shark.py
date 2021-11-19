
import unittest
from pysapets.shark import Shark
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SharkTest(unittest.TestCase):

  def setUp(self):
    self.shark = Shark()
    self.friends = [self.shark, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.shark.get_type(), constants.SHARK)

  # test that shark starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.shark.get_health(), 4)
  
  # test that shark starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.shark.get_attack(), 4)
  
  # test that initializing shark with additional health increases health
  def test_init_add_health(self):
    newShark = Shark(addHealth = 3)
    self.assertEqual(newShark.get_health(), 4 + 3)
  
  # test that initializing an shark with additional attack increases attack
  def test_init_add_attack(self):
    newShark = Shark(addAttack = 3)
    self.assertEqual(newShark.get_attack(), 4 + 3)
  
  # test that initializing shark with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newShark = Shark(addHealth = 3, addAttack = 3)
    self.assertEqual(newShark.get_health(), 4 + 3)
    self.assertEqual(newShark.get_attack(), 4 + 3)
  
  # test that shark ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.shark.get_ability_trigger(), constants.FAINT)
  
  # test that shark ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.shark.get_ability_triggeredBy(), constants.EACH_FRIEND)
  
  # TODO add relevant tests for shark ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      