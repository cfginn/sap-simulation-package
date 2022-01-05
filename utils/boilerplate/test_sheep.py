
import unittest
from pysapets.sheep import Sheep
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SheepTest(unittest.TestCase):

  def setUp(self):
    self.sheep = Sheep()
    self.friends = [self.sheep, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.sheep.get_type(), constants.SHEEP)

  # test that sheep starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.sheep.get_health(), 2)
  
  # test that sheep starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.sheep.get_attack(), 2)
  
  # test that initializing sheep with additional health increases health
  def test_init_add_health(self):
    newSheep = Sheep(addHealth = 3)
    self.assertEqual(newSheep.get_health(), 2 + 3)
  
  # test that initializing an sheep with additional attack increases attack
  def test_init_add_attack(self):
    newSheep = Sheep(addAttack = 3)
    self.assertEqual(newSheep.get_attack(), 2 + 3)
  
  # test that initializing sheep with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSheep = Sheep(addHealth = 3, addAttack = 3)
    self.assertEqual(newSheep.get_health(), 2 + 3)
    self.assertEqual(newSheep.get_attack(), 2 + 3)
  
  # test that sheep ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.sheep.get_ability_trigger(), constants.FAINT)
  
  # test that sheep ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.sheep.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for sheep ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      