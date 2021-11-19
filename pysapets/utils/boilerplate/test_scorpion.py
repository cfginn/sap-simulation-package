
import unittest
from pysapets.scorpion import Scorpion
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class ScorpionTest(unittest.TestCase):

  def setUp(self):
    self.scorpion = Scorpion()
    self.friends = [self.scorpion, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.scorpion.get_type(), constants.SCORPION)

  # test that scorpion starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.scorpion.get_health(), 1)
  
  # test that scorpion starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.scorpion.get_attack(), 1)
  
  # test that initializing scorpion with additional health increases health
  def test_init_add_health(self):
    newScorpion = Scorpion(addHealth = 3)
    self.assertEqual(newScorpion.get_health(), 1 + 3)
  
  # test that initializing an scorpion with additional attack increases attack
  def test_init_add_attack(self):
    newScorpion = Scorpion(addAttack = 3)
    self.assertEqual(newScorpion.get_attack(), 1 + 3)
  
  # test that initializing scorpion with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newScorpion = Scorpion(addHealth = 3, addAttack = 3)
    self.assertEqual(newScorpion.get_health(), 1 + 3)
    self.assertEqual(newScorpion.get_attack(), 1 + 3)
  
  # test that scorpion ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.scorpion.get_ability_trigger(), constants.KNOCK_OUT)
  
  # test that scorpion ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.scorpion.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for scorpion ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      