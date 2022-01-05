
import unittest
from pysapets.octopus import Octopus
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class OctopusTest(unittest.TestCase):

  def setUp(self):
    self.octopus = Octopus()
    self.friends = [self.octopus, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.octopus.get_type(), constants.OCTOPUS)

  # test that octopus starts with base health of 8
  def test_get_health(self):
    self.assertEqual(self.octopus.get_health(), 8)
  
  # test that octopus starts with base attack of 8 
  def test_get_attack(self):
    self.assertEqual(self.octopus.get_attack(), 8)
  
  # test that initializing octopus with additional health increases health
  def test_init_add_health(self):
    newOctopus = Octopus(addHealth = 3)
    self.assertEqual(newOctopus.get_health(), 8 + 3)
  
  # test that initializing an octopus with additional attack increases attack
  def test_init_add_attack(self):
    newOctopus = Octopus(addAttack = 3)
    self.assertEqual(newOctopus.get_attack(), 8 + 3)
  
  # test that initializing octopus with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newOctopus = Octopus(addHealth = 3, addAttack = 3)
    self.assertEqual(newOctopus.get_health(), 8 + 3)
    self.assertEqual(newOctopus.get_attack(), 8 + 3)
  
  # test that octopus ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.octopus.get_ability_trigger(), constants.LEVEL_UP)
  
  # test that octopus ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.octopus.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for octopus ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      