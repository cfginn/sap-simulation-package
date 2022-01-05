
import unittest
from pysapets.ram import Ram
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class RamTest(unittest.TestCase):

  def setUp(self):
    self.ram = Ram()
    self.friends = [self.ram, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.ram.get_type(), constants.RAM)

  # test that ram starts with base health of ?
  def test_get_health(self):
    self.assertEqual(self.ram.get_health(), ?)
  
  # test that ram starts with base attack of ? 
  def test_get_attack(self):
    self.assertEqual(self.ram.get_attack(), ?)
  
  # test that initializing ram with additional health increases health
  def test_init_add_health(self):
    newRam = Ram(addHealth = 3)
    self.assertEqual(newRam.get_health(), ? + 3)
  
  # test that initializing an ram with additional attack increases attack
  def test_init_add_attack(self):
    newRam = Ram(addAttack = 3)
    self.assertEqual(newRam.get_attack(), ? + 3)
  
  # test that initializing ram with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newRam = Ram(addHealth = 3, addAttack = 3)
    self.assertEqual(newRam.get_health(), ? + 3)
    self.assertEqual(newRam.get_attack(), ? + 3)
  
  # test that ram ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.ram.get_ability_trigger(), constants.END_OF_TURN_WITH_3_PLUS_GOLD)
  
  # test that ram ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.ram.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for ram ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      