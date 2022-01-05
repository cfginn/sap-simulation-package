
import unittest
from pysapets.mosquito import Mosquito
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class MosquitoTest(unittest.TestCase):

  def setUp(self):
    self.mosquito = Mosquito()
    self.friends = [self.mosquito]
    self.enemies = [Animal(3, 3), Animal(3, 3), Animal(3, 3), Animal(3, 3), Animal(3, 3)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.mosquito.get_type(), constants.MOSQUITO)

  # test that mosquito starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.mosquito.get_health(), 2)
  
  # test that mosquito starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.mosquito.get_attack(), 2)
  
  # test that initializing mosquito with additional health increases health
  def test_init_add_health(self):
    newMosquito = Mosquito(addHealth = 3)
    self.assertEqual(newMosquito.get_health(), 2 + 3)
  
  # test that initializing an mosquito with additional attack increases attack
  def test_init_add_attack(self):
    newMosquito = Mosquito(addAttack = 3)
    self.assertEqual(newMosquito.get_attack(), 2 + 3)
  
  # test that initializing mosquito with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newMosquito = Mosquito(addHealth = 3, addAttack = 3)
    self.assertEqual(newMosquito.get_health(), 2 + 3)
    self.assertEqual(newMosquito.get_attack(), 2 + 3)
  
  # test that mosquito ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.mosquito.get_ability_trigger(), constants.START_OF_BATTLE)
  
  # test that mosquito ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.mosquito.get_ability_triggeredBy(), constants.PLAYER)
  
  # TODO add relevant tests for mosquito ability
  # test that mosquito only hurts one enemy
  def test_run_ability(self):
    copyEnemies = deepcopy(self.enemies)
    self.mosquito.run_ability(enemies = self.enemies, friends = self.friends)
    
    enemyHurtFlag = False
    onlyOneEnemyHurtFlag = True
    for enemy, enemyCopy in zip(self.enemies, copyEnemies):
      if (enemy.get_health() < enemyCopy.get_health()):
        if enemyHurtFlag:
          onlyOneEnemyHurtFlag = False
        enemyHurtFlag = True

    self.assertTrue(onlyOneEnemyHurtFlag)
    self.assertTrue(enemyHurtFlag)

  def test_run_ability_level_1(self):
    copyEnemies = deepcopy(self.enemies)
    self.mosquito.run_ability(enemies = self.enemies, friends = self.friends)

    test = False
    for enemy, enemyCopy in zip(self.enemies, copyEnemies):
      if enemy.get_health() == enemyCopy.get_health() - 1:
        test = True
    
    self.assertTrue(test)

  def test_run_ability_level_2(self):
    copyEnemies = deepcopy(self.enemies)
    self.mosquito.level = 2
    self.mosquito.run_ability(enemies = self.enemies, friends = self.friends)

    test = [False, False]
    i = 0
    for enemy, enemyCopy in zip(self.enemies, copyEnemies):
      if enemy.get_health() == enemyCopy.get_health() - 1:
        test[i] = True
        i += 1
    
    self.assertTrue(test[0] and test[1])

  
  def test_run_ability_level_3(self):
    copyEnemies = deepcopy(self.enemies)
    self.mosquito.level = 3
    self.mosquito.run_ability(enemies = self.enemies, friends = self.friends)

    test = [False, False, False]
    i = 0
    for enemy, enemyCopy in zip(self.enemies, copyEnemies):
      if enemy.get_health() == enemyCopy.get_health() - 1:
        test[i] = True
        i += 1
    
    self.assertTrue(test[0] and test[1] and test[2])
    
      