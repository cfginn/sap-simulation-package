
import unittest
from pysapets.zombie_fly import Zombie_fly
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class Zombie_flyTest(unittest.TestCase):

  def setUp(self):
    self.zombie_fly = Zombie_fly()
    self.friends = [self.zombie_fly, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.zombie_fly.get_type(), constants.ZOMBIE_FLY)

  # test that zombie_fly starts with base health of ?
  def test_get_health(self):
    self.assertEqual(self.zombie_fly.get_health(), ?)
  
  # test that zombie_fly starts with base attack of ? 
  def test_get_attack(self):
    self.assertEqual(self.zombie_fly.get_attack(), ?)
  
  # test that initializing zombie_fly with additional health increases health
  def test_init_add_health(self):
    newZombie_fly = Zombie_fly(addHealth = 3)
    self.assertEqual(newZombie_fly.get_health(), ? + 3)
  
  # test that initializing an zombie_fly with additional attack increases attack
  def test_init_add_attack(self):
    newZombie_fly = Zombie_fly(addAttack = 3)
    self.assertEqual(newZombie_fly.get_attack(), ? + 3)
  
  # test that initializing zombie_fly with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newZombie_fly = Zombie_fly(addHealth = 3, addAttack = 3)
    self.assertEqual(newZombie_fly.get_health(), ? + 3)
    self.assertEqual(newZombie_fly.get_attack(), ? + 3)
  
  # test that zombie_fly ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.zombie_fly.get_ability_trigger(), constants.END_OF_TURN_WITH_3_PLUS_GOLD)
  
  # test that zombie_fly ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.zombie_fly.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for zombie_fly ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      