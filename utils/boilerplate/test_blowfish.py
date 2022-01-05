
import unittest
from pysapets.blowfish import Blowfish
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BlowfishTest(unittest.TestCase):

  def setUp(self):
    self.blowfish = Blowfish()
    self.friends = [self.blowfish, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.blowfish.get_type(), constants.BLOWFISH)

  # test that blowfish starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.blowfish.get_health(), 5)
  
  # test that blowfish starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.blowfish.get_attack(), 3)
  
  # test that initializing blowfish with additional health increases health
  def test_init_add_health(self):
    newBlowfish = Blowfish(addHealth = 3)
    self.assertEqual(newBlowfish.get_health(), 5 + 3)
  
  # test that initializing an blowfish with additional attack increases attack
  def test_init_add_attack(self):
    newBlowfish = Blowfish(addAttack = 3)
    self.assertEqual(newBlowfish.get_attack(), 3 + 3)
  
  # test that initializing blowfish with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBlowfish = Blowfish(addHealth = 3, addAttack = 3)
    self.assertEqual(newBlowfish.get_health(), 5 + 3)
    self.assertEqual(newBlowfish.get_attack(), 3 + 3)
  
  # test that blowfish ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.blowfish.get_ability_trigger(), constants.HURT)
  
  # test that blowfish ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.blowfish.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for blowfish ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      