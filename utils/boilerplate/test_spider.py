
import unittest
from pysapets.spider import Spider
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class SpiderTest(unittest.TestCase):

  def setUp(self):
    self.spider = Spider()
    self.friends = [self.spider, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.spider.get_type(), constants.SPIDER)

  # test that spider starts with base health of 2
  def test_get_health(self):
    self.assertEqual(self.spider.get_health(), 2)
  
  # test that spider starts with base attack of 2 
  def test_get_attack(self):
    self.assertEqual(self.spider.get_attack(), 2)
  
  # test that initializing spider with additional health increases health
  def test_init_add_health(self):
    newSpider = Spider(addHealth = 3)
    self.assertEqual(newSpider.get_health(), 2 + 3)
  
  # test that initializing an spider with additional attack increases attack
  def test_init_add_attack(self):
    newSpider = Spider(addAttack = 3)
    self.assertEqual(newSpider.get_attack(), 2 + 3)
  
  # test that initializing spider with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    newSpider = Spider(addHealth = 3, addAttack = 3)
    self.assertEqual(newSpider.get_health(), 2 + 3)
    self.assertEqual(newSpider.get_attack(), 2 + 3)
  
  # test that spider ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.spider.get_ability_trigger(), constants.FAINT)
  
  # test that spider ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.spider.get_ability_triggeredBy(), constants.SELF)
  
  # TODO add relevant tests for spider ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      