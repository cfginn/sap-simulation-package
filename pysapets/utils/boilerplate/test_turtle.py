
import unittest
from pysapets.turtle import Turtle
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class TurtleTest(unittest.TestCase):

  def setUp(self):
    self.turtle = Turtle()
    self.friends = [self.turtle, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.turtle.get_type(), constants.TURTLE)

  # test that turtle starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.turtle.get_health(), 4)
  
  # test that turtle starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.turtle.get_attack(), 2)
  
  # test that initializing turtle with additional health increases health
  def test_init_add_health(self):
    newTurtle = Turtle(addHealth = 3)
    self.assertEqual(newTurtle.get_health(), 4 + 3)
  
  # test that initializing an turtle with additional attack increases attack
  def test_init_add_attack(self):
    newTurtle = Turtle(addAttack = 3)
    self.assertEqual(newTurtle.get_attack(), 2 + 3)
  
  # test that initializing turtle with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newTurtle = Turtle(addHealth = 3, addAttack = 3)
    self.assertEqual(newTurtle.get_health(), 4 + 3)
    self.assertEqual(newTurtle.get_attack(), 2 + 3)
  
  # test that turtle ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.turtle.get_ability_trigger(), constants.FAINT)
  
  # test that turtle ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.turtle.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for turtle ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      