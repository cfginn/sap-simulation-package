
import unittest
from pysapets.fish import Fish
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class FishTest(unittest.TestCase):

  def setUp(self):
    self.fish = Fish()
    self.friends = [self.fish, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.fish.get_type(), constants.FISH)

  # test that fish starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.fish.get_health(), 3)
  
  # test that fish starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.fish.get_attack(), 2)
  
  # test that initializing fish with additional health increases health
  def test_init_add_health(self):
    newFish = Fish(addHealth = 3)
    self.assertEqual(newFish.get_health(), 3 + 3)
  
  # test that initializing an fish with additional attack increases attack
  def test_init_add_attack(self):
    newFish = Fish(addAttack = 3)
    self.assertEqual(newFish.get_attack(), 2 + 3)
  
  # test that initializing fish with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newFish = Fish(addHealth = 3, addAttack = 3)
    self.assertEqual(newFish.get_health(), 3 + 3)
    self.assertEqual(newFish.get_attack(), 2 + 3)
  
  # test that fish ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.fish.get_ability_trigger(), constants.LEVEL_UP)
  
  # test that fish ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.fish.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for fish ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      