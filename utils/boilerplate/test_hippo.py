
import unittest
from pysapets.hippo import Hippo
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class HippoTest(unittest.TestCase):

  def setUp(self):
    self.hippo = Hippo()
    self.friends = [self.hippo, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.hippo.get_type(), constants.HIPPO)

  # test that hippo starts with base health of 7
  def test_get_health(self):
    self.assertEqual(self.hippo.get_health(), 7)
  
  # test that hippo starts with base attack of 4 
  def test_get_attack(self):
    self.assertEqual(self.hippo.get_attack(), 4)
  
  # test that initializing hippo with additional health increases health
  def test_init_add_health(self):
    newHippo = Hippo(addHealth = 3)
    self.assertEqual(newHippo.get_health(), 7 + 3)
  
  # test that initializing an hippo with additional attack increases attack
  def test_init_add_attack(self):
    newHippo = Hippo(addAttack = 3)
    self.assertEqual(newHippo.get_attack(), 4 + 3)
  
  # test that initializing hippo with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newHippo = Hippo(addHealth = 3, addAttack = 3)
    self.assertEqual(newHippo.get_health(), 7 + 3)
    self.assertEqual(newHippo.get_attack(), 4 + 3)
  
  # test that hippo ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.hippo.get_ability_trigger(), constants.KNOCK_OUT)
  
  # test that hippo ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.hippo.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for hippo ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      