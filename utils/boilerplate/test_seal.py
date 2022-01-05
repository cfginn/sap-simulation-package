
import unittest
from pysapets.seal import Seal
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SealTest(unittest.TestCase):

  def setUp(self):
    self.seal = Seal()
    self.friends = [self.seal, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.seal.get_type(), constants.SEAL)

  # test that seal starts with base health of 6
  def test_get_health(self):
    self.assertEqual(self.seal.get_health(), 6)
  
  # test that seal starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.seal.get_attack(), 3)
  
  # test that initializing seal with additional health increases health
  def test_init_add_health(self):
    newSeal = Seal(addHealth = 3)
    self.assertEqual(newSeal.get_health(), 6 + 3)
  
  # test that initializing an seal with additional attack increases attack
  def test_init_add_attack(self):
    newSeal = Seal(addAttack = 3)
    self.assertEqual(newSeal.get_attack(), 3 + 3)
  
  # test that initializing seal with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSeal = Seal(addHealth = 3, addAttack = 3)
    self.assertEqual(newSeal.get_health(), 6 + 3)
    self.assertEqual(newSeal.get_attack(), 3 + 3)
  
  # test that seal ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.seal.get_ability_trigger(), constants.EATS_SHOP_FOOD)
  
  # test that seal ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.seal.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for seal ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      