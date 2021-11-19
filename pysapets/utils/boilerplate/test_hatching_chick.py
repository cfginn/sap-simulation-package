
import unittest
from pysapets.hatching_chick import Hatching_chick
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class Hatching_chickTest(unittest.TestCase):

  def setUp(self):
    self.hatching_chick = Hatching_chick()
    self.friends = [self.hatching_chick, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.hatching_chick.get_type(), constants.HATCHING_CHICK)

  # test that hatching_chick starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.hatching_chick.get_health(), 1)
  
  # test that hatching_chick starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.hatching_chick.get_attack(), 1)
  
  # test that initializing hatching_chick with additional health increases health
  def test_init_add_health(self):
    newHatching_chick = Hatching_chick(addHealth = 3)
    self.assertEqual(newHatching_chick.get_health(), 1 + 3)
  
  # test that initializing an hatching_chick with additional attack increases attack
  def test_init_add_attack(self):
    newHatching_chick = Hatching_chick(addAttack = 3)
    self.assertEqual(newHatching_chick.get_attack(), 1 + 3)
  
  # test that initializing hatching_chick with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newHatching_chick = Hatching_chick(addHealth = 3, addAttack = 3)
    self.assertEqual(newHatching_chick.get_health(), 1 + 3)
    self.assertEqual(newHatching_chick.get_attack(), 1 + 3)
  
  # test that hatching_chick ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.hatching_chick.get_ability_trigger(), constants.END_OF_TURN)
  
  # test that hatching_chick ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.hatching_chick.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for hatching_chick ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      