
import unittest
from pysapets.lobster import Lobster
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class LobsterTest(unittest.TestCase):

  def setUp(self):
    self.lobster = Lobster()
    self.friends = [self.lobster, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.lobster.get_type(), constants.LOBSTER)

  # test that lobster starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.lobster.get_health(), 3)
  
  # test that lobster starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.lobster.get_attack(), 3)
  
  # test that initializing lobster with additional health increases health
  def test_init_add_health(self):
    newLobster = Lobster(addHealth = 3)
    self.assertEqual(newLobster.get_health(), 3 + 3)
  
  # test that initializing an lobster with additional attack increases attack
  def test_init_add_attack(self):
    newLobster = Lobster(addAttack = 3)
    self.assertEqual(newLobster.get_attack(), 3 + 3)
  
  # test that initializing lobster with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newLobster = Lobster(addHealth = 3, addAttack = 3)
    self.assertEqual(newLobster.get_health(), 3 + 3)
    self.assertEqual(newLobster.get_attack(), 3 + 3)
  
  # test that lobster ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.lobster.get_ability_trigger(), constants.SUMMONED)
  
  # test that lobster ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.lobster.get_ability_triggeredBy(), constants.EACH_FRIEND)
  
  # TODO add relevant tests for lobster ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      