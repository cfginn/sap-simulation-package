
import unittest
from pysapets.zombie_cricket import Zombie_cricket
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class Zombie_cricketTest(unittest.TestCase):

  def setUp(self):
    self.zombie_cricket = Zombie_cricket()
    self.friends = [self.zombie_cricket, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.zombie_cricket.get_type(), constants.ZOMBIE_CRICKET)

  # test that zombie_cricket starts with base health of ?
  def test_get_health(self):
    self.assertEqual(self.zombie_cricket.get_health(), ?)
  
  # test that zombie_cricket starts with base attack of ? 
  def test_get_attack(self):
    self.assertEqual(self.zombie_cricket.get_attack(), ?)
  
  # test that initializing zombie_cricket with additional health increases health
  def test_init_add_health(self):
    newZombie_cricket = Zombie_cricket(addHealth = 3)
    self.assertEqual(newZombie_cricket.get_health(), ? + 3)
  
  # test that initializing an zombie_cricket with additional attack increases attack
  def test_init_add_attack(self):
    newZombie_cricket = Zombie_cricket(addAttack = 3)
    self.assertEqual(newZombie_cricket.get_attack(), ? + 3)
  
  # test that initializing zombie_cricket with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newZombie_cricket = Zombie_cricket(addHealth = 3, addAttack = 3)
    self.assertEqual(newZombie_cricket.get_health(), ? + 3)
    self.assertEqual(newZombie_cricket.get_attack(), ? + 3)
  
  # test that zombie_cricket ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.zombie_cricket.get_ability_trigger(), constants.END_OF_TURN_WITH_3_PLUS_GOLD)
  
  # test that zombie_cricket ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.zombie_cricket.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for zombie_cricket ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      