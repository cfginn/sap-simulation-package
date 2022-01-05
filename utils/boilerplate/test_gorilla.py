
import unittest
from pysapets.gorilla import Gorilla
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class GorillaTest(unittest.TestCase):

  def setUp(self):
    self.gorilla = Gorilla()
    self.friends = [self.gorilla, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.gorilla.get_type(), constants.GORILLA)

  # test that gorilla starts with base health of 6
  def test_get_health(self):
    self.assertEqual(self.gorilla.get_health(), 6)
  
  # test that gorilla starts with base attack of 6 
  def test_get_attack(self):
    self.assertEqual(self.gorilla.get_attack(), 6)
  
  # test that initializing gorilla with additional health increases health
  def test_init_add_health(self):
    newGorilla = Gorilla(addHealth = 3)
    self.assertEqual(newGorilla.get_health(), 6 + 3)
  
  # test that initializing an gorilla with additional attack increases attack
  def test_init_add_attack(self):
    newGorilla = Gorilla(addAttack = 3)
    self.assertEqual(newGorilla.get_attack(), 6 + 3)
  
  # test that initializing gorilla with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newGorilla = Gorilla(addHealth = 3, addAttack = 3)
    self.assertEqual(newGorilla.get_health(), 6 + 3)
    self.assertEqual(newGorilla.get_attack(), 6 + 3)
  
  # test that gorilla ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.gorilla.get_ability_trigger(), constants.HURT)
  
  # test that gorilla ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.gorilla.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for gorilla ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      