
import unittest
from pysapets.bus import Bus
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BusTest(unittest.TestCase):

  def setUp(self):
    self.bus = Bus()
    self.friends = [self.bus, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.bus.get_type(), constants.BUS)

  # test that bus starts with base health of ?
  def test_get_health(self):
    self.assertEqual(self.bus.get_health(), ?)
  
  # test that bus starts with base attack of ? 
  def test_get_attack(self):
    self.assertEqual(self.bus.get_attack(), ?)
  
  # test that initializing bus with additional health increases health
  def test_init_add_health(self):
    newBus = Bus(addHealth = 3)
    self.assertEqual(newBus.get_health(), ? + 3)
  
  # test that initializing an bus with additional attack increases attack
  def test_init_add_attack(self):
    newBus = Bus(addAttack = 3)
    self.assertEqual(newBus.get_attack(), ? + 3)
  
  # test that initializing bus with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBus = Bus(addHealth = 3, addAttack = 3)
    self.assertEqual(newBus.get_health(), ? + 3)
    self.assertEqual(newBus.get_attack(), ? + 3)
  
  # test that bus ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.bus.get_ability_trigger(), constants.END_OF_TURN_WITH_3_PLUS_GOLD)
  
  # test that bus ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.bus.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for bus ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      