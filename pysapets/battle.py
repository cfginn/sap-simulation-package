import pysapets.constants as constants
from pysapets.animal import Animal


class Battle():

  def __init__(self, teamA, teamB):
    self.teamA = teamA
    self.teamB = teamB

    self.result = 0

  def attack(self):
    attackerA = self.teamA[-1]
    attackerB = self.teamB[-1]

    attackerA.subtract_health(attackerB.attack)
    attackerB.subtract_health(attackerA.attack)

    _check_for_abilities(self.teamA, self.teamB)
    _check_for_abilities(self.teamB, self.teamA)

  def start(self):
    _check_for_start_of_battle(self.teamA, self.teamB)
    _check_for_start_of_battle(self.teamB, self.teamA)

    for animal in self.teamA:
      if animal.is_dead():
        _handle_faint(animal, self.teamA, self.teamB)

    for animal in self.teamB:
      if animal.is_dead():
        _handle_faint(animal, self.teamB, self.teamA)

    while len(self.teamA) > 0 and len(self.teamB) > 0:
      self.attack()
    
    if len(self.teamA) == 0: 
      self.result -= 1
    
    if len(self.teamB) == 0:
      self.result += 1
    
    return self.result

def _check_for_abilities(friends, enemies):
  attacker = friends[-1]

  if attacker.is_dead():
    _handle_faint(attacker, friends, enemies)
  
  for animal in friends:
    if animal.is_dead():
      _handle_faint(animal, friends, enemies)
    

def _check_for_start_of_battle(friends, enemies):
  for animal in friends:
    if animal.get_ability_trigger() == constants.START_OF_BATTLE:
      animal.run_ability(friends = friends, enemies = enemies)

def _handle_faint(dead_animal, friends, enemies):
  indexOfDeadAnimal = friends.index(dead_animal)

  if dead_animal.get_ability_trigger() == constants.FAINT and dead_animal.get_ability_triggeredBy() == constants.SELF:
    dead_animal.run_ability(friends = friends, enemies = enemies)

    # if the animal is not dead, then new animal was summoned
    if friends[indexOfDeadAnimal].is_dead():
      friends.pop()
    else:
      for animal in friends:
        if animal.get_ability_trigger() == constants.SUMMONED and animal.get_ability_triggeredBy() == constants.EACH_FRIEND:
          animal.run_ability(friends = friends, enemies = enemies, summoned = friends[-1])
  
  else:
    friends.pop(indexOfDeadAnimal)