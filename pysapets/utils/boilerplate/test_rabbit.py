
import unittest
from pysapets.rabbit import Rabbit
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class RabbitTest(unittest.TestCase):

  def setUp(self):
    self.rabbit = Rabbit()
    self.friends = [self.rabbit, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.rabbit.get_type(), constants.RABBIT)

  # test that rabbit starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.rabbit.get_health(), 2)
  
  # test that rabbit starts with base attack of 3 
  def test_get_attack(self):
    self.assertEqual(self.rabbit.get_attack(), 3)
  
  # test that initializing rabbit with additional health increases health
  def test_init_add_health(self):
    newRabbit = Rabbit(addHealth = 3)
    self.assertEqual(newRabbit.get_health(), 2 + 3)
  
  # test that initializing an rabbit with additional attack increases attack
  def test_init_add_attack(self):
    newRabbit = Rabbit(addAttack = 3)
    self.assertEqual(newRabbit.get_attack(), 3 + 3)
  
  # test that initializing rabbit with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newRabbit = Rabbit(addHealth = 3, addAttack = 3)
    self.assertEqual(newRabbit.get_health(), 2 + 3)
    self.assertEqual(newRabbit.get_attack(), 3 + 3)
  
  # test that rabbit ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.rabbit.get_ability_trigger(), constants.EATS_SHOP_FOOD)
  
  # test that rabbit ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.rabbit.get_ability_triggeredBy(), constants.EACH_FRIEND)
  
  # TODO add relevant tests for rabbit ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      