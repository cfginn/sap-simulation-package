
import unittest
from pysapets.swan import Swan
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SwanTest(unittest.TestCase):

  def setUp(self):
    self.swan = Swan()
    self.friends = [self.swan, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.swan.get_type(), constants.SWAN)

  # test that swan starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.swan.get_health(), 4)
  
  # test that swan starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.swan.get_attack(), 3)
  
  # test that initializing swan with additional health increases health
  def test_init_add_health(self):
    newSwan = Swan(addHealth = 3)
    self.assertEqual(newSwan.get_health(), 4 + 3)
  
  # test that initializing an swan with additional attack increases attack
  def test_init_add_attack(self):
    newSwan = Swan(addAttack = 3)
    self.assertEqual(newSwan.get_attack(), 3 + 3)
  
  # test that initializing swan with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSwan = Swan(addHealth = 3, addAttack = 3)
    self.assertEqual(newSwan.get_health(), 4 + 3)
    self.assertEqual(newSwan.get_attack(), 3 + 3)
  
  # test that swan ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.swan.get_ability_trigger(), constants.START_OF_TURN)
  
  # test that swan ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.swan.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for swan ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      