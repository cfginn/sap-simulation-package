
import unittest
from pysapets.tropical_fish import Tropical_fish
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class Tropical_fishTest(unittest.TestCase):

  def setUp(self):
    self.tropical_fish = Tropical_fish()
    self.friends = [self.tropical_fish, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.tropical_fish.get_type(), constants.TROPICAL_FISH)

  # test that tropical_fish starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.tropical_fish.get_health(), 4)
  
  # test that tropical_fish starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.tropical_fish.get_attack(), 2)
  
  # test that initializing tropical_fish with additional health increases health
  def test_init_add_health(self):
    newTropical_fish = Tropical_fish(addHealth = 3)
    self.assertEqual(newTropical_fish.get_health(), 4 + 3)
  
  # test that initializing an tropical_fish with additional attack increases attack
  def test_init_add_attack(self):
    newTropical_fish = Tropical_fish(addAttack = 3)
    self.assertEqual(newTropical_fish.get_attack(), 2 + 3)
  
  # test that initializing tropical_fish with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newTropical_fish = Tropical_fish(addHealth = 3, addAttack = 3)
    self.assertEqual(newTropical_fish.get_health(), 4 + 3)
    self.assertEqual(newTropical_fish.get_attack(), 2 + 3)
  
  # test that tropical_fish ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.tropical_fish.get_ability_trigger(), constants.END_OF_TURN)
  
  # test that tropical_fish ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.tropical_fish.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for tropical_fish ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      