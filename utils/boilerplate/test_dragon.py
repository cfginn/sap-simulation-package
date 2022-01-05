
import unittest
from pysapets.dragon import Dragon
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class DragonTest(unittest.TestCase):

  def setUp(self):
    self.dragon = Dragon()
    self.friends = [self.dragon, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.dragon.get_type(), constants.DRAGON)

  # test that dragon starts with base health of 8
  def test_get_health(self):
    self.assertEqual(self.dragon.get_health(), 8)
  
  # test that dragon starts with base attack of 6 
  def test_get_attack(self):
    self.assertEqual(self.dragon.get_attack(), 6)
  
  # test that initializing dragon with additional health increases health
  def test_init_add_health(self):
    newDragon = Dragon(addHealth = 3)
    self.assertEqual(newDragon.get_health(), 8 + 3)
  
  # test that initializing an dragon with additional attack increases attack
  def test_init_add_attack(self):
    newDragon = Dragon(addAttack = 3)
    self.assertEqual(newDragon.get_attack(), 6 + 3)
  
  # test that initializing dragon with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newDragon = Dragon(addHealth = 3, addAttack = 3)
    self.assertEqual(newDragon.get_health(), 8 + 3)
    self.assertEqual(newDragon.get_attack(), 6 + 3)
  
  # test that dragon ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.dragon.get_ability_trigger(), constants.BUY_TIER_1_ANIMAL)
  
  # test that dragon ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.dragon.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for dragon ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      