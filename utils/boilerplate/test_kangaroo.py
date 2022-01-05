
import unittest
from pysapets.kangaroo import Kangaroo
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class KangarooTest(unittest.TestCase):

  def setUp(self):
    self.kangaroo = Kangaroo()
    self.friends = [self.kangaroo, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.kangaroo.get_type(), constants.KANGAROO)

  # test that kangaroo starts with base health of 3
  def test_get_health(self):
    self.assertEqual(self.kangaroo.get_health(), 3)
  
  # test that kangaroo starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.kangaroo.get_attack(), 2)
  
  # test that initializing kangaroo with additional health increases health
  def test_init_add_health(self):
    newKangaroo = Kangaroo(addHealth = 3)
    self.assertEqual(newKangaroo.get_health(), 3 + 3)
  
  # test that initializing an kangaroo with additional attack increases attack
  def test_init_add_attack(self):
    newKangaroo = Kangaroo(addAttack = 3)
    self.assertEqual(newKangaroo.get_attack(), 2 + 3)
  
  # test that initializing kangaroo with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newKangaroo = Kangaroo(addHealth = 3, addAttack = 3)
    self.assertEqual(newKangaroo.get_health(), 3 + 3)
    self.assertEqual(newKangaroo.get_attack(), 2 + 3)
  
  # test that kangaroo ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.kangaroo.get_ability_trigger(), constants.AFTER_ATTACK)
  
  # test that kangaroo ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.kangaroo.get_ability_triggeredBy(), constants.FRIEND_AHEAD)
  
  # TODO add relevant tests for kangaroo ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      