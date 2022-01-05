
import unittest
from pysapets.dog import Dog
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class DogTest(unittest.TestCase):

  def setUp(self):
    self.dog = Dog()
    self.friends = [self.dog, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.dog.get_type(), constants.DOG)

  # test that dog starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.dog.get_health(), 2)
  
  # test that dog starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.dog.get_attack(), 2)
  
  # test that initializing dog with additional health increases health
  def test_init_add_health(self):
    newDog = Dog(addHealth = 3)
    self.assertEqual(newDog.get_health(), 2 + 3)
  
  # test that initializing an dog with additional attack increases attack
  def test_init_add_attack(self):
    newDog = Dog(addAttack = 3)
    self.assertEqual(newDog.get_attack(), 2 + 3)
  
  # test that initializing dog with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newDog = Dog(addHealth = 3, addAttack = 3)
    self.assertEqual(newDog.get_health(), 2 + 3)
    self.assertEqual(newDog.get_attack(), 2 + 3)
  
  # test that dog ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.dog.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that dog ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.dog.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for dog ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      