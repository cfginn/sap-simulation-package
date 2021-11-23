# import and and ant class
import unittest
from pysapets.ant import Ant
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

# create a class called AntTest that inherits from the unittest.TestCase class
class AntTest(unittest.TestCase):

  # initialize an ant and friends in setup
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
  
  # test that initializing an ant with additional health increases health
  def test_init_add_health(self):
    newAnt = Ant(addHealth = 3)
    self.assertEqual(newAnt.get_health(), 4)
  
  # test that initializing an ant with additional attack increases attack
  def test_init_add_attack(self):
    newAnt = Ant(addAttack = 3)
    self.assertEqual(newAnt.get_attack(), 5)
  
  # test that initializing an ant with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newAnt = Ant(addHealth = 3, addAttack = 3)
    self.assertEqual(newAnt.get_health(), 4)
    self.assertEqual(newAnt.get_attack(), 5)
  
  # test that ant ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.ant.get_ability_trigger(), constants.FAINT)
  
  # test that ant ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.ant.get_ability_triggeredBy(), constants.SELF)
  
  # test that ant ability does not work on dead pets
  def test_ability_print_message_all_dead(self):
    for friend in self.friends:
      friend.subtract_health(friend.get_health())

    copy_of_dead_friends = deepcopy(self.friends)
    self.ant.run_ability(friends = self.friends)
    for friend, friend_copy in zip(self.friends, copy_of_dead_friends):
      self.assertEqual(friend.get_health(), friend_copy.get_health())
      self.assertEqual(friend.get_attack(), friend_copy.get_attack())

  # test that ability does not affect other pets if still alive
  def test_run_ability_no_effect(self):
    copy_of_friends = self.friends.copy()
    self.ant.run_ability(friends = self.friends)
    for friend, friend_copy in zip(self.friends, copy_of_friends):
      self.assertEqual(friend.get_health(), friend_copy.get_health())
      self.assertEqual(friend.get_attack(), friend_copy.get_attack())

  # test that ant ability does not buff itself
  def test_run_ability_self(self):
    init_attack = self.ant.get_attack()
    self.ant.subtract_health(self.ant.get_health())
    self.ant.run_ability(friends = self.friends)
    self.assertEqual(self.ant.get_health(), 0)
    self.assertEqual(self.ant.get_attack(), init_attack)

  # test that ant ability effect funtion adds health and attack to one friend
  def test_run_ability(self):
    animal_buffed = False
    only_one_buffed = True
    copy_of_friends = deepcopy(self.friends)
    self.ant.subtract_health(self.ant.get_health())
    self.ant.run_ability(friends = self.friends)
    for friend, friend_copy in zip(self.friends, copy_of_friends):
      if friend.get_health() > friend_copy.get_health() and friend.get_attack() > friend_copy.get_attack():
        if animal_buffed:
          only_one_buffed = False
        animal_buffed = True
    self.assertTrue(animal_buffed)
    self.assertTrue(only_one_buffed)

  # test that ant ability adds correct buff at level 1
  def test_run_ability_level_1(self):
    level_1_correct = False

    copy_of_friends_level_1 = deepcopy(self.friends)
    
    self.ant.subtract_health(self.ant.get_health())
    self.ant.run_ability(friends = self.friends)

    for friend, friend_copy in zip(self.friends, copy_of_friends_level_1):
      if friend.get_health() == friend_copy.get_health() + 1 and friend.get_attack() == friend_copy.get_attack() + 2:
        level_1_correct = True
      
    self.assertTrue(level_1_correct)


  # test that ant ability adds correct buff at level 2
  def test_run_ability_level_2(self):
    level_2_correct = False

    copy_of_friends_level_2 = deepcopy(self.friends)

    self.ant.subtract_health(self.ant.get_health())
    self.ant.run_ability(friends = self.friends)

    for friend, friend_copy in zip(self.friends, copy_of_friends_level_2):
      if friend.get_health() == friend_copy.get_health() + 1 and friend.get_attack() == friend_copy.get_attack() + 2:
        level_2_correct = True

    self.assertTrue(level_2_correct)
  
  # test that ant ability adds correct buff at level 3
  def test_run_ability_level_3(self):
    level_3_correct = False

    copy_of_friends_level_3 = deepcopy(self.friends)

    self.ant.subtract_health(self.ant.get_health())
    self.ant.run_ability(friends = self.friends)

    for friend, friend_copy in zip(self.friends, copy_of_friends_level_3):
      if friend.get_health() == friend_copy.get_health() + 1 and friend.get_attack() == friend_copy.get_attack() + 2:
        level_3_correct = True

    self.assertTrue(level_3_correct)

  # test that ant ability does not affect other pets if they are dead