
import unittest
from pysapets.cricket import Cricket
from pysapets.zombie_cricket import ZombieCricket
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class ZombieCricketTest(unittest.TestCase):

  def setUp(self):
    self.cricket = Cricket()
    self.zombie_cricket = ZombieCricket(self.cricket)
    self.friends = [self.zombie_cricket, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.zombie_cricket.get_type(), constants.ZOMBIE_CRICKET)

  # test that zombie_cricket starts with base health of ?
  def test_get_health(self):
    self.assertEqual(self.zombie_cricket.get_health(), 1)
  
  # test that zombie_cricket starts with base attack of ? 
  def test_get_attack(self):
    self.assertEqual(self.zombie_cricket.get_attack(), 1)
  
  # test that initializing zombie_cricket with additional health increases health
  def test_init_add_health(self):
    newZombieCricket = ZombieCricket(self.cricket, addHealth = 3)
    self.assertEqual(newZombieCricket.get_health(), 1 + 3)
  
  # test that initializing an zombie_cricket with additional attack increases attack
  def test_init_add_attack(self):
    newZombieCricket = ZombieCricket(self.cricket, addAttack = 3)
    self.assertEqual(newZombieCricket.get_attack(), 1 + 3)
  
  # test that initializing zombie_cricket with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newZombieCricket = ZombieCricket(self.cricket, addHealth = 3, addAttack = 3)
    self.assertEqual(newZombieCricket.get_health(), 1 + 3)
    self.assertEqual(newZombieCricket.get_attack(), 1 + 3)
  
  # test that zombie_cricket ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.zombie_cricket.get_ability_trigger(), None)
  
  # test that zombie_cricket ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.zombie_cricket.get_ability_triggeredBy(), None)

  # test that zombie cricket has 2 health and attack when spawned by lvl 2 cricket
  def test_spawn_lvl_2(self):
    self.newCricket = Cricket()
    self.newCricket.level = 2
    self.newZombieCricket = ZombieCricket(self.newCricket)

    self.assertEqual(self.newZombieCricket.get_health(), 2)
    self.assertEqual(self.newZombieCricket.get_attack(), 2)

  # test that zombie cricket has 3 health and attack when spawned by lvl 3 cricket
  def test_spawn_lvl_3(self):
    self.newCricket = Cricket()
    self.newCricket.level = 3
    self.newZombieCricket = ZombieCricket(self.newCricket)

    self.assertEqual(self.newZombieCricket.get_health(), 3)
    self.assertEqual(self.newZombieCricket.get_attack(), 3)
    
      