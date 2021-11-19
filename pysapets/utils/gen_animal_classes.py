import json
from util_funcs import get_json_from_api, camel_to_snake, dash_to_snake_ignore_first

json_data = get_json_from_api()

for animal, obj in json_data["pets"].items():
  tier = obj["tier"]

  if tier != "summon": 
    upper_animal = dash_to_snake_ignore_first(animal)
    lower_animal = upper_animal.lower()
    capitalized_animal = lower_animal.capitalize()
    base_attack = obj["baseAttack"]
    base_health = obj["baseHealth"]
    if "level1Ability" in obj:
      if "description" in obj["level1Ability"]:
        level1_ability_desc = obj["level1Ability"]["description"]
      if "trigger" in obj["level1Ability"]:
        trigger = camel_to_snake(obj["level1Ability"]["trigger"])

      if "triggeredBy" in obj["level1Ability"] and "kind" in obj["level1Ability"]["triggeredBy"]:
        triggered_by = camel_to_snake(obj["level1Ability"]["triggeredBy"]["kind"])

    if "level2Ability" in obj:
      if "description" in obj["level2Ability"]:
        level2_ability_desc = obj["level2Ability"]["description"]

    if "level3Ability" in obj:
      if "description" in obj["level3Ability"]:
        level3_ability_desc = obj["level3Ability"]["description"]

    with open("./boilerplate/test_{}.py".format(lower_animal), "w") as test_file:
      test_file.write("""
import unittest
from pysapets.{lower_animal} import {capitalized_animal}
from pysapets.animal import Animal
import pysapets.constants as constants
from unittest.mock import patch
from io import StringIO
from copy import deepcopy

class {capitalized_animal}Test(unittest.TestCase):

  def setUp(self):
    self.{lower_animal} = {capitalized_animal}()
    self.friends = [self.{lower_animal}, Animal(2, 2), Animal(2, 2), Animal(2, 2), Animal(2, 2)]
  
  # test that get_type returns the correct type
  def test_get_type(self):
    self.assertEqual(self.{lower_animal}.get_type(), constants.{upper_animal})

  # test that {lower_animal} starts with base health of {base_health}
  def test_get_health(self):
    self.assertEqual(self.{lower_animal}.get_health(), {base_health})
  
  # test that {lower_animal} starts with base attack of {base_attack} 
  def test_get_attack(self):
    self.assertEqual(self.{lower_animal}.get_attack(), {base_attack})
  
  # test that initializing {lower_animal} with additional health increases health
  def test_init_add_health(self):
    new{capitalized_animal} = {capitalized_animal}(addHealth = 3)
    self.assertEqual(new{capitalized_animal}.get_health(), {base_health} + 3)
  
  # test that initializing an {lower_animal} with additional attack increases attack
  def test_init_add_attack(self):
    new{capitalized_animal} = {capitalized_animal}(addAttack = 3)
    self.assertEqual(new{capitalized_animal}.get_attack(), {base_attack} + 3)
  
  # test that initializing {lower_animal} with additional health and attack increases health and attack
  def test_init_add_health_attack(self):
    new{capitalized_animal} = {capitalized_animal}(addHealth = 3, addAttack = 3)
    self.assertEqual(new{capitalized_animal}.get_health(), {base_health} + 3)
    self.assertEqual(new{capitalized_animal}.get_attack(), {base_attack} + 3)
  
  # test that {lower_animal} ability has correct trigger
  def test_get_ability_trigger(self):
    self.assertEqual(self.{lower_animal}.get_ability_trigger(), constants.{trigger})
  
  # test that {lower_animal} ability has correct triggeredBy
  def test_get_ability_triggeredBy(self):
    self.assertEqual(self.{lower_animal}.get_ability_triggeredBy(), constants.{triggered_by})
  
  # TODO add relevant tests for {lower_animal} ability

  def test_run_ability(self):
    pass

  def test_run_ability_level_1(self):
    pass

  def test_run_ability_level_2(self):
    pass
  
  def test_run_ability_level_3(self):
    pass
    
    
      """.format(tier = tier, lower_animal=lower_animal, upper_animal=upper_animal, base_attack=base_attack, base_health=base_health, trigger=trigger, triggered_by=triggered_by, capitalized_animal=capitalized_animal, level1_ability_desc=level1_ability_desc, level2_ability_desc=level2_ability_desc, level3_ability_desc=level3_ability_desc))

    with open("./boilerplate/{}.py".format(lower_animal), "w") as class_file:
      class_file.write("""
from pysapets.animal import Animal
import pysapets.constants as constants
import random

class {capitalized_animal}(Animal):
  # base health and attack values
  BASE_ATTACK = {base_attack} 
  BASE_HEALTH = {base_health} 
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # lvl 1: {level1_ability_desc}
    # lvl 2: {level2_ability_desc}
    # lvl 3: {level3_ability_desc}
    def _run_effect(self, friends):
      pass
    
    # create ability
    self.ability = Animal.Ability(self, constants.{trigger}, constants.{triggered_by}, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.{upper_animal}, tier = {tier}, ability=self.ability)

      """.format(tier = tier, lower_animal=lower_animal, upper_animal=upper_animal, base_attack=base_attack, base_health=base_health, trigger=trigger, triggered_by=triggered_by, capitalized_animal=capitalized_animal, level1_ability_desc=level1_ability_desc, level2_ability_desc=level2_ability_desc, level3_ability_desc=level3_ability_desc))
