
import unittest
from pysapets.ant import Ant
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class AntTest(unittest.TestCase):

  def setUp(self):
    self.ant = Ant()
    self.friends = [self.ant, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.ant.get_type(), constants.ANT)

  # test that ant starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.ant.get_health(), 1)
  
  # test that ant starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.ant.get_attack(), 2)
  
  # test that initializing ant with additional health increases health
  def test_init_add_health(self):
    newAnt = Ant(addHealth = 3)
    self.assertEqual(newAnt.get_health(), 1 + 3)
  
  # test that initializing an ant with additional attack increases attack
  def test_init_add_attack(self):
    newAnt = Ant(addAttack = 3)
    self.assertEqual(newAnt.get_attack(), 2 + 3)
  
  # test that initializing ant with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newAnt = Ant(addHealth = 3, addAttack = 3)
    self.assertEqual(newAnt.get_health(), 1 + 3)
    self.assertEqual(newAnt.get_attack(), 2 + 3)
  
  # test that ant ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.ant.get_ability_trigger(), constants.FAINT)
  
  # test that ant ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.ant.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for ant ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      