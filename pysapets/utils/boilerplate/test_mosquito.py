
import unittest
from pysapets.mosquito import Mosquito
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class MosquitoTest(unittest.TestCase):

  def setUp(self):
    self.mosquito = Mosquito()
    self.friends = [self.mosquito, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.mosquito.get_type(), constants.MOSQUITO)

  # test that mosquito starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.mosquito.get_health(), 2)
  
  # test that mosquito starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.mosquito.get_attack(), 2)
  
  # test that initializing mosquito with additional health increases health
  def test_init_add_health(self):
    newMosquito = Mosquito(addHealth = 3)
    self.assertEqual(newMosquito.get_health(), 2 + 3)
  
  # test that initializing an mosquito with additional attack increases attack
  def test_init_add_attack(self):
    newMosquito = Mosquito(addAttack = 3)
    self.assertEqual(newMosquito.get_attack(), 2 + 3)
  
  # test that initializing mosquito with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newMosquito = Mosquito(addHealth = 3, addAttack = 3)
    self.assertEqual(newMosquito.get_health(), 2 + 3)
    self.assertEqual(newMosquito.get_attack(), 2 + 3)
  
  # test that mosquito ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.mosquito.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that mosquito ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.mosquito.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for mosquito ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      