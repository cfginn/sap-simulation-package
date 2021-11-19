
import unittest
from pysapets.giraffe import Giraffe
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class GiraffeTest(unittest.TestCase):

  def setUp(self):
    self.giraffe = Giraffe()
    self.friends = [self.giraffe, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.giraffe.get_type(), constants.GIRAFFE)

  # test that giraffe starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.giraffe.get_health(), 3)
  
  # test that giraffe starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.giraffe.get_attack(), 1)
  
  # test that initializing giraffe with additional health increases health
  def test_init_add_health(self):
    newGiraffe = Giraffe(addHealth = 3)
    self.assertEqual(newGiraffe.get_health(), 3 + 3)
  
  # test that initializing an giraffe with additional attack increases attack
  def test_init_add_attack(self):
    newGiraffe = Giraffe(addAttack = 3)
    self.assertEqual(newGiraffe.get_attack(), 1 + 3)
  
  # test that initializing giraffe with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newGiraffe = Giraffe(addHealth = 3, addAttack = 3)
    self.assertEqual(newGiraffe.get_health(), 3 + 3)
    self.assertEqual(newGiraffe.get_attack(), 1 + 3)
  
  # test that giraffe ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.giraffe.get_ability_trigger(), constants.END_OF_TURN)
  
  # test that giraffe ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.giraffe.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for giraffe ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      