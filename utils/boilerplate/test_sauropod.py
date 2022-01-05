
import unittest
from pysapets.sauropod import Sauropod
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SauropodTest(unittest.TestCase):

  def setUp(self):
    self.sauropod = Sauropod()
    self.friends = [self.sauropod, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.sauropod.get_type(), constants.SAUROPOD)

  # test that sauropod starts with base health of 12
  def test_get_health(self):
    self.assertEqual(self.sauropod.get_health(), 12)
  
  # test that sauropod starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.sauropod.get_attack(), 4)
  
  # test that initializing sauropod with additional health increases health
  def test_init_add_health(self):
    newSauropod = Sauropod(addHealth = 3)
    self.assertEqual(newSauropod.get_health(), 12 + 3)
  
  # test that initializing an sauropod with additional attack increases attack
  def test_init_add_attack(self):
    newSauropod = Sauropod(addAttack = 3)
    self.assertEqual(newSauropod.get_attack(), 4 + 3)
  
  # test that initializing sauropod with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSauropod = Sauropod(addHealth = 3, addAttack = 3)
    self.assertEqual(newSauropod.get_health(), 12 + 3)
    self.assertEqual(newSauropod.get_attack(), 4 + 3)
  
  # test that sauropod ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.sauropod.get_ability_trigger(), constants.BUY_FOOD)
  
  # test that sauropod ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.sauropod.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for sauropod ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      