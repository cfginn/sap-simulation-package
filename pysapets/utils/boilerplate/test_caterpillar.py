
import unittest
from pysapets.caterpillar import Caterpillar
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class CaterpillarTest(unittest.TestCase):

  def setUp(self):
    self.caterpillar = Caterpillar()
    self.friends = [self.caterpillar, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.caterpillar.get_type(), constants.CATERPILLAR)

  # test that caterpillar starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.caterpillar.get_health(), 4)
  
  # test that caterpillar starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.caterpillar.get_attack(), 1)
  
  # test that initializing caterpillar with additional health increases health
  def test_init_add_health(self):
    newCaterpillar = Caterpillar(addHealth = 3)
    self.assertEqual(newCaterpillar.get_health(), 4 + 3)
  
  # test that initializing an caterpillar with additional attack increases attack
  def test_init_add_attack(self):
    newCaterpillar = Caterpillar(addAttack = 3)
    self.assertEqual(newCaterpillar.get_attack(), 1 + 3)
  
  # test that initializing caterpillar with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newCaterpillar = Caterpillar(addHealth = 3, addAttack = 3)
    self.assertEqual(newCaterpillar.get_health(), 4 + 3)
    self.assertEqual(newCaterpillar.get_attack(), 1 + 3)
  
  # test that caterpillar ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.caterpillar.get_ability_trigger(), constants.START_OF_TURN)
  
  # test that caterpillar ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.caterpillar.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for caterpillar ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      