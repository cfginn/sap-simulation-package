
import unittest
from pysapets.ladybug import Ladybug
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class LadybugTest(unittest.TestCase):

  def setUp(self):
    self.ladybug = Ladybug()
    self.friends = [self.ladybug, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.ladybug.get_type(), constants.LADYBUG)

  # test that ladybug starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.ladybug.get_health(), 3)
  
  # test that ladybug starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.ladybug.get_attack(), 1)
  
  # test that initializing ladybug with additional health increases health
  def test_init_add_health(self):
    newLadybug = Ladybug(addHealth = 3)
    self.assertEqual(newLadybug.get_health(), 3 + 3)
  
  # test that initializing an ladybug with additional attack increases attack
  def test_init_add_attack(self):
    newLadybug = Ladybug(addAttack = 3)
    self.assertEqual(newLadybug.get_attack(), 1 + 3)
  
  # test that initializing ladybug with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newLadybug = Ladybug(addHealth = 3, addAttack = 3)
    self.assertEqual(newLadybug.get_health(), 3 + 3)
    self.assertEqual(newLadybug.get_attack(), 1 + 3)
  
  # test that ladybug ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.ladybug.get_ability_trigger(), constants.BUY_FOOD)
  
  # test that ladybug ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.ladybug.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for ladybug ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      