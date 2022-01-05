
import unittest
from pysapets.elephant import Elephant
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class ElephantTest(unittest.TestCase):

  def setUp(self):
    self.elephant = Elephant()
    self.friends = [self.elephant, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.elephant.get_type(), constants.ELEPHANT)

  # test that elephant starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.elephant.get_health(), 5)
  
  # test that elephant starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.elephant.get_attack(), 3)
  
  # test that initializing elephant with additional health increases health
  def test_init_add_health(self):
    newElephant = Elephant(addHealth = 3)
    self.assertEqual(newElephant.get_health(), 5 + 3)
  
  # test that initializing an elephant with additional attack increases attack
  def test_init_add_attack(self):
    newElephant = Elephant(addAttack = 3)
    self.assertEqual(newElephant.get_attack(), 3 + 3)
  
  # test that initializing elephant with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newElephant = Elephant(addHealth = 3, addAttack = 3)
    self.assertEqual(newElephant.get_health(), 5 + 3)
    self.assertEqual(newElephant.get_attack(), 3 + 3)
  
  # test that elephant ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.elephant.get_ability_trigger(), constants.BEFORE_ATTACK)
  
  # test that elephant ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.elephant.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for elephant ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      