
import unittest
from pysapets.parrot import Parrot
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class ParrotTest(unittest.TestCase):

  def setUp(self):
    self.parrot = Parrot()
    self.friends = [self.parrot, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.parrot.get_type(), constants.PARROT)

  # test that parrot starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.parrot.get_health(), 2)
  
  # test that parrot starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.parrot.get_attack(), 3)
  
  # test that initializing parrot with additional health increases health
  def test_init_add_health(self):
    newParrot = Parrot(addHealth = 3)
    self.assertEqual(newParrot.get_health(), 2 + 3)
  
  # test that initializing an parrot with additional attack increases attack
  def test_init_add_attack(self):
    newParrot = Parrot(addAttack = 3)
    self.assertEqual(newParrot.get_attack(), 3 + 3)
  
  # test that initializing parrot with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newParrot = Parrot(addHealth = 3, addAttack = 3)
    self.assertEqual(newParrot.get_health(), 2 + 3)
    self.assertEqual(newParrot.get_attack(), 3 + 3)
  
  # test that parrot ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.parrot.get_ability_trigger(), constants.END_OF_TURN)
  
  # test that parrot ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.parrot.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for parrot ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      