
import unittest
from pysapets.tyrannosaurus import Tyrannosaurus
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class TyrannosaurusTest(unittest.TestCase):

  def setUp(self):
    self.tyrannosaurus = Tyrannosaurus()
    self.friends = [self.tyrannosaurus, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.tyrannosaurus.get_type(), constants.TYRANNOSAURUS)

  # test that tyrannosaurus starts with base health of 4
  def test_get_health(self):
    self.assertEqual(self.tyrannosaurus.get_health(), 4)
  
  # test that tyrannosaurus starts with base attack of 9 
  def test_get_attack(self):
    self.assertEqual(self.tyrannosaurus.get_attack(), 9)
  
  # test that initializing tyrannosaurus with additional health increases health
  def test_init_add_health(self):
    newTyrannosaurus = Tyrannosaurus(addHealth = 3)
    self.assertEqual(newTyrannosaurus.get_health(), 4 + 3)
  
  # test that initializing an tyrannosaurus with additional attack increases attack
  def test_init_add_attack(self):
    newTyrannosaurus = Tyrannosaurus(addAttack = 3)
    self.assertEqual(newTyrannosaurus.get_attack(), 9 + 3)
  
  # test that initializing tyrannosaurus with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newTyrannosaurus = Tyrannosaurus(addHealth = 3, addAttack = 3)
    self.assertEqual(newTyrannosaurus.get_health(), 4 + 3)
    self.assertEqual(newTyrannosaurus.get_attack(), 9 + 3)
  
  # test that tyrannosaurus ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.tyrannosaurus.get_ability_trigger(), constants.END_OF_TURN_WITH_3_PLUS_GOLD)
  
  # test that tyrannosaurus ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.tyrannosaurus.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for tyrannosaurus ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      