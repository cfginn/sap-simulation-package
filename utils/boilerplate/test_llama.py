
import unittest
from pysapets.llama import Llama
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class LlamaTest(unittest.TestCase):

  def setUp(self):
    self.llama = Llama()
    self.friends = [self.llama, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.llama.get_type(), constants.LLAMA)

  # test that llama starts with base health of 5
  def test_get_health(self):
    self.assertEqual(self.llama.get_health(), 5)
  
  # test that llama starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.llama.get_attack(), 2)
  
  # test that initializing llama with additional health increases health
  def test_init_add_health(self):
    newLlama = Llama(addHealth = 3)
    self.assertEqual(newLlama.get_health(), 5 + 3)
  
  # test that initializing an llama with additional attack increases attack
  def test_init_add_attack(self):
    newLlama = Llama(addAttack = 3)
    self.assertEqual(newLlama.get_attack(), 2 + 3)
  
  # test that initializing llama with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newLlama = Llama(addHealth = 3, addAttack = 3)
    self.assertEqual(newLlama.get_health(), 5 + 3)
    self.assertEqual(newLlama.get_attack(), 2 + 3)
  
  # test that llama ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.llama.get_ability_trigger(), constants.END_OF_TURN_WITH_4_OR_LESS_ANIMALS)
  
  # test that llama ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.llama.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for llama ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      