
import unittest
from pysapets.snake import Snake
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SnakeTest(unittest.TestCase):

  def setUp(self):
    self.snake = Snake()
    self.friends = [self.snake, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.snake.get_type(), constants.SNAKE)

  # test that snake starts with base health of 6
  def test_get_health(self):
    self.assertEqual(self.snake.get_health(), 6)
  
  # test that snake starts with base attack of 6 
  def test_get_attack(self):
    self.assertEqual(self.snake.get_attack(), 6)
  
  # test that initializing snake with additional health increases health
  def test_init_add_health(self):
    newSnake = Snake(addHealth = 3)
    self.assertEqual(newSnake.get_health(), 6 + 3)
  
  # test that initializing an snake with additional attack increases attack
  def test_init_add_attack(self):
    newSnake = Snake(addAttack = 3)
    self.assertEqual(newSnake.get_attack(), 6 + 3)
  
  # test that initializing snake with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSnake = Snake(addHealth = 3, addAttack = 3)
    self.assertEqual(newSnake.get_health(), 6 + 3)
    self.assertEqual(newSnake.get_attack(), 6 + 3)
  
  # test that snake ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.snake.get_ability_trigger(), constants.AFTER_ATTACK)
  
  # test that snake ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.snake.get_ability_triggeredBy(), constants.FRIEND_AHEAD)
  
  # TODO add relevant tests for snake ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      