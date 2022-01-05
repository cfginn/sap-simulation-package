import pysapets.constants as constants
from pysapets.animal import Animal


class Battle():

  def __init__(self, teamA, teamB):
    self.teamA = teamA
    self.teamB = teamB

    self.result = 0

  def attack(self):
    self.print_teams()

    attackerA = self.teamA[-1]
    attackerB = self.teamB[-1]

    index_of_A = self.teamA.index(attackerA)
    index_of_B = self.teamB.index(attackerB)

    type_of_A = attackerA.get_type()
    type_of_B = attackerB.get_type()

    attackerA.subtract_health(attackerB.attack)
    attackerB.subtract_health(attackerA.attack)

    print('A-{}-{} took {} damage!'.format(index_of_A, type_of_A, attackerB.attack))
    print('B-{}-{} took {} damage!'.format(index_of_B, type_of_B, attackerA.attack))

    _check_for_abilities(self.teamA, self.teamB, "A", "B")
    _check_for_abilities(self.teamB, self.teamA, "B", "A")

  def start(self):
    self.print_teams()

    _check_for_start_of_battle(self.teamA, self.teamB, "A", "B")
    _check_for_start_of_battle(self.teamB, self.teamA, "B", "A")

    for animal in self.teamA:
      if animal.is_dead():
        _handle_faint(animal, self.teamA, self.teamB, "A", "B")

    for animal in self.teamB:
      if animal.is_dead():
        _handle_faint(animal, self.teamB, self.teamA, "B", "A")

    while len(self.teamA) > 0 and len(self.teamB) > 0:
      self.attack()
    
    if len(self.teamA) == 0: 
      self.result -= 1
    
    if len(self.teamB) == 0:
      self.result += 1

    self.print_result()
    
    return self.result
  
  def __str__(self):
    return f'Team A: {self.teamA}\nTeam B: {self.teamB}'

  def print_teams(self):
    print("******************************")
    print(self)
    print("******************************")

  def print_result(self):
    if self.result == 0:
      print("It's a tie!")
    elif self.result == 1:
      print("Team A wins!")
    elif self.result == -1:
      print("Team B wins!")

# helper functions

def _check_for_abilities(friends, enemies, teamName, otherTeamName):
  attacker = friends[-1]

  if attacker.is_dead():
    _handle_faint(attacker, friends, enemies, teamName, otherTeamName)
  
  for animal in friends:
    if animal.is_dead():
      _handle_faint(animal, friends, enemies, teamName, otherTeamName)
    

def _check_for_start_of_battle(friends, enemies, teamName, otherTeamName):
  for animal in friends:
    if animal.get_ability_trigger() == constants.START_OF_BATTLE:
      animal.run_ability(friends = friends, enemies = enemies, teamName = teamName, otherTeamName = otherTeamName)

def _handle_faint(dead_animal, friends, enemies, teamName, otherTeamName):
  indexOfDeadAnimal = friends.index(dead_animal)

  print("{}-{}-{} fainted!".format(teamName, indexOfDeadAnimal, dead_animal.get_type()))

  if dead_animal.get_ability_trigger() == constants.FAINT and dead_animal.get_ability_triggeredBy() == constants.SELF:
    dead_animal.run_ability(friends = friends, enemies = enemies, teamName = teamName, otherTeamName = otherTeamName)

    # if the animal is not dead, then new animal was summoned
    if friends[indexOfDeadAnimal].is_dead():
      friends.pop(indexOfDeadAnimal)
    else:
      for animal in friends:
        if animal.get_ability_trigger() == constants.SUMMONED and animal.get_ability_triggeredBy() == constants.EACH_FRIEND:
          animal.run_ability(friends = friends, enemies = enemies, summoned = friends[-1], teamName = teamName, otherTeamName = otherTeamName)
  
  else:
    friends.pop(indexOfDeadAnimal)