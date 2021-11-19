
import unittest
from pysapets.leopard import Leopard
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class LeopardTest(unittest.TestCase):

  def setUp(self):
    self.leopard = Leopard()
    self.friends = [self.leopard, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.leopard.get_type(), constants.LEOPARD)

  # test that leopard starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.leopard.get_health(), 4)
  
  # test that leopard starts with base attack of 6 
  def test_get_attack(self):
    self.assertEqual(self.leopard.get_attack(), 6)
  
  # test that initializing leopard with additional health increases health
  def test_init_add_health(self):
    newLeopard = Leopard(addHealth = 3)
    self.assertEqual(newLeopard.get_health(), 4 + 3)
  
  # test that initializing an leopard with additional attack increases attack
  def test_init_add_attack(self):
    newLeopard = Leopard(addAttack = 3)
    self.assertEqual(newLeopard.get_attack(), 6 + 3)
  
  # test that initializing leopard with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newLeopard = Leopard(addHealth = 3, addAttack = 3)
    self.assertEqual(newLeopard.get_health(), 4 + 3)
    self.assertEqual(newLeopard.get_attack(), 6 + 3)
  
  # test that leopard ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.leopard.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that leopard ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.leopard.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for leopard ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      