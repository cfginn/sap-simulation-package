
import unittest
from pysapets.bison import Bison
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BisonTest(unittest.TestCase):

  def setUp(self):
    self.bison = Bison()
    self.friends = [self.bison, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.bison.get_type(), constants.BISON)

  # test that bison starts with base health of 6
  def test_get_health(self):
    self.assertEqual(self.bison.get_health(), 6)
  
  # test that bison starts with base attack of 6 
  def test_get_attack(self):
    self.assertEqual(self.bison.get_attack(), 6)
  
  # test that initializing bison with additional health increases health
  def test_init_add_health(self):
    newBison = Bison(addHealth = 3)
    self.assertEqual(newBison.get_health(), 6 + 3)
  
  # test that initializing an bison with additional attack increases attack
  def test_init_add_attack(self):
    newBison = Bison(addAttack = 3)
    self.assertEqual(newBison.get_attack(), 6 + 3)
  
  # test that initializing bison with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBison = Bison(addHealth = 3, addAttack = 3)
    self.assertEqual(newBison.get_health(), 6 + 3)
    self.assertEqual(newBison.get_attack(), 6 + 3)
  
  # test that bison ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.bison.get_ability_trigger(), constants.END_OF_TURN_WITH_LVL_3_FRIEND)
  
  # test that bison ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.bison.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for bison ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      