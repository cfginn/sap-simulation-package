
import unittest
from pysapets.puppy import Puppy
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class PuppyTest(unittest.TestCase):

  def setUp(self):
    self.puppy = Puppy()
    self.friends = [self.puppy, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.puppy.get_type(), constants.PUPPY)

  # test that puppy starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.puppy.get_health(), 1)
  
  # test that puppy starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.puppy.get_attack(), 1)
  
  # test that initializing puppy with additional health increases health
  def test_init_add_health(self):
    newPuppy = Puppy(addHealth = 3)
    self.assertEqual(newPuppy.get_health(), 1 + 3)
  
  # test that initializing an puppy with additional attack increases attack
  def test_init_add_attack(self):
    newPuppy = Puppy(addAttack = 3)
    self.assertEqual(newPuppy.get_attack(), 1 + 3)
  
  # test that initializing puppy with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newPuppy = Puppy(addHealth = 3, addAttack = 3)
    self.assertEqual(newPuppy.get_health(), 1 + 3)
    self.assertEqual(newPuppy.get_attack(), 1 + 3)
  
  # test that puppy ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.puppy.get_ability_trigger(), constants.END_OF_TURN_WITH_2_PLUS_GOLD)
  
  # test that puppy ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.puppy.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for puppy ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      