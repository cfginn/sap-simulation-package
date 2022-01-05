
import unittest
from pysapets.owl import Owl
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class OwlTest(unittest.TestCase):

  def setUp(self):
    self.owl = Owl()
    self.friends = [self.owl, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.owl.get_type(), constants.OWL)

  # test that owl starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.owl.get_health(), 3)
  
  # test that owl starts with base attack of 5 
  def test_get_attack(self):
    self.assertEqual(self.owl.get_attack(), 5)
  
  # test that initializing owl with additional health increases health
  def test_init_add_health(self):
    newOwl = Owl(addHealth = 3)
    self.assertEqual(newOwl.get_health(), 3 + 3)
  
  # test that initializing an owl with additional attack increases attack
  def test_init_add_attack(self):
    newOwl = Owl(addAttack = 3)
    self.assertEqual(newOwl.get_attack(), 5 + 3)
  
  # test that initializing owl with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newOwl = Owl(addHealth = 3, addAttack = 3)
    self.assertEqual(newOwl.get_health(), 3 + 3)
    self.assertEqual(newOwl.get_attack(), 5 + 3)
  
  # test that owl ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.owl.get_ability_trigger(), constants.SELL)
  
  # test that owl ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.owl.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for owl ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      