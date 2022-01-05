
import unittest
from pysapets.bee import Bee
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class BeeTest(unittest.TestCase):

  def setUp(self):
    self.bee = Bee()
    self.friends = [self.bee, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.bee.get_type(), constants.BEE)

  # test that bee starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.bee.get_health(), 1)
  
  # test that bee starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.bee.get_attack(), 1)
  
  # test that initializing bee with additional health increases health
  def test_init_add_health(self):
    newBee = Bee(addHealth = 3)
    self.assertEqual(newBee.get_health(), 1 + 3)
  
  # test that initializing an bee with additional attack increases attack
  def test_init_add_attack(self):
    newBee = Bee(addAttack = 3)
    self.assertEqual(newBee.get_attack(), 1 + 3)
  
  # test that initializing bee with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newBee = Bee(addHealth = 3, addAttack = 3)
    self.assertEqual(newBee.get_health(), 1 + 3)
    self.assertEqual(newBee.get_attack(), 1 + 3)
  
  # test that bee ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.bee.get_ability_trigger(), constants.SUMMONED)
  
  # test that bee ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.bee.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for bee ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      