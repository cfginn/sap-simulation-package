
import unittest
from pysapets.horse import Horse
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class HorseTest(unittest.TestCase):

  def setUp(self):
    self.horse = Horse()
    self.summoned = Animal(2, 2)
    self.friends = [self.horse, self.summoned, Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.horse.get_type(), constants.HORSE)

  # test that horse starts with base health of 1
  def test_get_health(self):
    self.assertEqual(self.horse.get_health(), 1)
  
  # test that horse starts with base attack of 1 
  def test_get_attack(self):
    self.assertEqual(self.horse.get_attack(), 2)
  
  # test that initializing horse with additional health increases health
  def test_init_add_health(self):
    newHorse = Horse(addHealth = 3)
    self.assertEqual(newHorse.get_health(), 1 + 3)
  
  # test that initializing an horse with additional attack increases attack
  def test_init_add_attack(self):
    newHorse = Horse(addAttack = 3)
    self.assertEqual(newHorse.get_attack(), 2 + 3)
  
  # test that initializing horse with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newHorse = Horse(addHealth = 3, addAttack = 3)
    self.assertEqual(newHorse.get_health(), 1 + 3)
    self.assertEqual(newHorse.get_attack(), 2 + 3)
  
  # test that ability can not be run if horse is dead
  def test_run_ability_dead(self):
    copyOfSummoned = deepcopy(self.summoned)
    self.horse.subtract_health(self.horse.get_health())
    self.horse.run_ability(summoned = self.summoned, friends = self.friends)

    self.assertEqual(copyOfSummoned.get_attack(), self.summoned.get_attack())
  
  # test that horse ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.horse.get_ability_trigger(), constants.SUMMONED)
  
  # test that horse ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.horse.get_ability_triggeredBy(), constants.EACH_FRIEND)

  def test_run_ability_level_1(self):
    copyOfSummoned = deepcopy(self.summoned)
    self.horse.run_ability(summoned = self.summoned, friends = self.friends)

    self.assertEqual(self.summoned.get_attack(), copyOfSummoned.get_attack() + 1)

  def test_run_ability_level_2(self):
    copyOfSummoned = deepcopy(self.summoned)
    self.horse.level = 2
    self.horse.run_ability(summoned = self.summoned, friends = self.friends)

    self.assertEqual(self.summoned.get_attack(), copyOfSummoned.get_attack() + 2)
  
  def test_run_ability_level_3(self):
    copyOfSummoned = deepcopy(self.summoned)
    self.horse.level = 3
    self.horse.run_ability(summoned = self.summoned, friends = self.friends)

    self.assertEqual(self.summoned.get_attack(), copyOfSummoned.get_attack() + 3)
    
      