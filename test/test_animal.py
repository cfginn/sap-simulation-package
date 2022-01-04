import unittest

# Import the class Animal from the animal.py file
from pysapets.animal import Animal
from pysapets.constants import MELON_ARMOR, POISON_ATTACK

# Create a class called AnimalTest that inherits from the unittest.TestCase class
class AnimalTest(unittest.TestCase):
  # initialize an animal in setup
  def setUp(self):
    self.animal = Animal(2, 2)
  
  # test that the animal's level is 1
  def test_animal_level(self):
    self.assertEqual(self.animal.level, 1)

  # test that the animal's experience is 0
  def test_animal_experience(self):
    self.assertEqual(self.animal.experience, 0)

  # test get_health
  def test_animal_get_health(self):
    self.assertEqual(self.animal.get_health(), 2)
  
  # test get_attack
  def test_animal_get_attack(self):
    self.assertEqual(self.animal.get_attack(), 2)
  
  # test get_level
  def test_animal_get_level(self):
    self.assertEqual(self.animal.get_level(), 1)

  # test get_experience
  def test_animal_get_experience(self):
    self.assertEqual(self.animal.get_experience(), 0)
  
  #test get_tier
  def test_animal_get_tier(self):
    self.assertEqual(self.animal.tier, 1)

  # test print(animal)
  def test_animal_print(self):
    self.assertEqual(str(self.animal), 'Animal(A: 2, H: 2, L: 1, E: 0)')

  # test add_experience
  def test_animal_add_experience(self):
    self.animal.add_experience(1)
    self.assertEqual(self.animal.experience, 1)

  # test that the animal's level is 2 after it 2 experience
  def test_animal_level_up(self):
    self.animal.add_experience(2)
    self.assertEqual(self.animal.level, 2)

  # test that 1 experience does not level up the animal
  def test_animal_level_up_experience(self):
    self.animal.add_experience(1)
    self.assertEqual(self.animal.level, 1)
  
  # test that the animals level is 3 after 5 experience
  def test_animal_level_up_experience_multiple(self):
    self.animal.add_experience(5)
    self.assertEqual(self.animal.level, 3)
  
  # test that experience is maxed at 5
  def test_animal_level_up_experience_max(self):
    self.animal.add_experience(6)
    self.assertEqual(self.animal.experience, 5)
  
  # test that the animals level is 1 after 0 experience
  def test_animal_level_up_experience_zero(self):
    self.animal.add_experience(0)
    self.assertEqual(self.animal.level, 1)
  
  # test add_health
  def test_animal_add_health(self):
    self.animal.add_health(1)
    self.assertEqual(self.animal.health, 3)

  # test add_attack
  def test_animal_add_attack(self):
    self.animal.add_attack(1)
    self.assertEqual(self.animal.attack, 3)
  
  # test subtract_health
  def test_animal_subtract_health(self):
    self.animal.subtract_health(1)
    self.assertEqual(self.animal.health, 1)

  # test that subtract_health does not go below 0
  def test_animal_subtract_health_zero(self):
    self.animal.subtract_health(3)
    self.assertEqual(self.animal.health, 0)
  
  # test is_dead
  def test_animal_is_dead(self):
    self.assertFalse(self.animal.is_dead())

  # test add status
  def test_animal_add_status(self):
    self.animal.add_status(POISON_ATTACK)
    self.assertEqual(self.animal.status, POISON_ATTACK)
  
  # test remove status
  def test_animal_remove_status(self):
    self.animal.add_status(POISON_ATTACK)
    self.animal.remove_status()
    self.assertEqual(self.animal.status, None)

  # test get_status
  def test_animal_get_status(self):
    self.animal.add_status(POISON_ATTACK)
    self.assertEqual(self.animal.get_status(), POISON_ATTACK)
  
  # test that adding new status removes old status
  def test_animal_add_status_remove_status(self):
    self.animal.add_status(POISON_ATTACK)
    self.animal.add_status(MELON_ARMOR)
    self.assertNotEqual(self.animal.status, POISON_ATTACK)

  # test that adding new status keeps new status
  def test_animal_add_status_keep_status(self):
    self.animal.add_status(POISON_ATTACK)
    self.animal.add_status(MELON_ARMOR)
    self.assertEqual(self.animal.status, MELON_ARMOR)
  
  # test is_dead after dying
  def test_animal_dead_is_dead(self):
    self.animal.subtract_health(2)
    self.assertTrue(self.animal.is_dead())

  # test that animal is dead when health is 0
  def test_animal_dead(self):
    self.animal.subtract_health(2)
    self.assertTrue(self.animal.dead)
  
  # test get animal type
  def test_animal_get_type(self):
    self.assertEqual(self.animal.get_type(), 'Animal')

# Run the tests
if __name__ == '__main__':
  unittest.main()