
import unittest
from pysapets.bluebird import Bluebird
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BluebirdTest(unittest.TestCase):

  def setUp(self):
    self.bluebird = Bluebird()
    self.friends = [self.bluebird, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.bluebird.get_type(), constants.BLUEBIRD)

  # test that bluebird starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.bluebird.get_health(), 1)
  
  # test that bluebird starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.bluebird.get_attack(), 2)
  
  # test that initializing bluebird with additional health increases health
  def test_init_add_health(self):
    newBluebird = Bluebird(addHealth = 3)
    self.assertEqual(newBluebird.get_health(), 1 + 3)
  
  # test that initializing an bluebird with additional attack increases attack
  def test_init_add_attack(self):
    newBluebird = Bluebird(addAttack = 3)
    self.assertEqual(newBluebird.get_attack(), 2 + 3)
  
  # test that initializing bluebird with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBluebird = Bluebird(addHealth = 3, addAttack = 3)
    self.assertEqual(newBluebird.get_health(), 1 + 3)
    self.assertEqual(newBluebird.get_attack(), 2 + 3)
  
  # test that bluebird ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.bluebird.get_ability_trigger(), constants.END_OF_TURN)
  
  # test that bluebird ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.bluebird.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for bluebird ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      