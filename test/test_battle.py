import unittest
from pysapets.battle import Battle
from pysapets.animal import Animal
from copy import deepcopy
from unittest.mock import Mock
import pysapets.constants as constants

class BattleTest(unittest.TestCase):
    
  def setUp(self):
    self.teamA = [Animal(1,2), Animal(1,2), Animal(1,2), Animal(1,2), Animal(1,2)]
    self.teamB = [Animal(1,2), Animal(1,2), Animal(1,2), Animal(1,2), Animal(1,2)]

    self.battle = Battle(self.teamA, self.teamB)

  
  # test that attack decreases each animal's health by the correct amount
  def test_attack(self):
    copyOfTeamA = deepcopy(self.teamA)
    copyOfTeamB = deepcopy(self.teamB)
    self.battle.attack()
    self.assertEqual(self.teamA[-1].health, copyOfTeamA[-1].health - self.teamB[-1].attack)
    self.assertEqual(self.teamB[-1].health, copyOfTeamB[-1].health - self.teamA[-1].attack)
  
  # test that animal is removed from team when dead
  def test_remove_dead(self):
    self.battle.teamA[-1].health = 1
    self.battle.attack()

    self.assertEqual(len(self.battle.teamA), 4)
  
  # test that starting battle with empty teams leads to draw
  def test_empty_teams(self):
    battle = Battle([], [])
    result = battle.start()
    self.assertEqual(result, 0)

  # test that starting battle with one empty team leads to win for other team
  def test_one_empty_team(self):
    battle = Battle([], self.teamB)
    result = battle.start()
    self.assertEqual(result, -1)
  
  # test that animal with faint ability is has ability called
  def test_faint_ability(self):
    mockedAnimal = self.battle.teamA[-1] = Mock()
    mockedAnimal.get_ability_trigger.return_value = constants.FAINT
    mockedAnimal.get_ability_triggeredBy.return_value = constants.SELF
    mockedAnimal.health = 1
    mockedAnimal.attack = 1

    self.battle.start()

    mockedAnimal.run_ability.assert_called_once()
  
  def test_summon_ability(self):
    def summon_animal(**kwargs):
      friends = kwargs['friends']
      summoned_animal = Animal(50, 50)
      friends[-1] = summoned_animal

    mockedAnimal = self.battle.teamA[-1] = Mock()
    mockedAnimal.get_ability_trigger.return_value = constants.FAINT
    mockedAnimal.get_ability_triggeredBy.return_value = constants.SELF
    mockedAnimal.health = 1
    mockedAnimal.attack = 1
    mockedAnimal.run_ability = summon_animal

    self.battle.attack()

    self.assertEqual(self.teamA[-1].health, 50)

  def test_start_of_battle_ability(self):

    mockedAnimal = self.battle.teamA[-1] = Mock()
    mockedAnimal.get_ability_trigger.return_value = constants.START_OF_BATTLE
    mockedAnimal.health = 1
    mockedAnimal.attack = 1

    self.battle.start()

    mockedAnimal.run_ability.assert_called_once()

  # def test_enemy_in_mid_getting_sniped(self):
  #   def snipe_enemy(**kwargs):
  #     enemies = kwargs['enemies']
  #     enemies[2].subtract_health(30)
    
  #   mockedAnimal = self.battle.teamA[-1] = Mock()
  #   mockedAnimal.get_ability_trigger.return_value = constants.START_OF_BATTLE
  #   mockedAnimal.health = 1
  #   mockedAnimal.attack = 1
  #   mockedAnimal.run_ability = snipe_enemy

  def test_when_friend_summoned_ability(self):
    pass


