
import unittest
from pysapets.hedgehog import Hedgehog
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class HedgehogTest(unittest.TestCase):

  def setUp(self):
    self.hedgehog = Hedgehog()
    self.friends = [self.hedgehog, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.hedgehog.get_type(), constants.HEDGEHOG)

  # test that hedgehog starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.hedgehog.get_health(), 2)
  
  # test that hedgehog starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.hedgehog.get_attack(), 3)
  
  # test that initializing hedgehog with additional health increases health
  def test_init_add_health(self):
    newHedgehog = Hedgehog(addHealth = 3)
    self.assertEqual(newHedgehog.get_health(), 2 + 3)
  
  # test that initializing an hedgehog with additional attack increases attack
  def test_init_add_attack(self):
    newHedgehog = Hedgehog(addAttack = 3)
    self.assertEqual(newHedgehog.get_attack(), 3 + 3)
  
  # test that initializing hedgehog with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newHedgehog = Hedgehog(addHealth = 3, addAttack = 3)
    self.assertEqual(newHedgehog.get_health(), 2 + 3)
    self.assertEqual(newHedgehog.get_attack(), 3 + 3)
  
  # test that hedgehog ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.hedgehog.get_ability_trigger(), constants.FAINT)
  
  # test that hedgehog ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.hedgehog.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for hedgehog ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      