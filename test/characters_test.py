import unittest

from src.character import Character


class CharactersTest(unittest.TestCase):

    def test_health_starting_at_1000(self):
        character = Character()
        self.assertEqual(character.health, 1000)

    def test_level_starting_at_1(self):
        character = Character()
        self.assertEqual(character.level, 1)

    def test_starting_alive(self):
        character = Character()
        self.assertTrue(character.is_alive())

    def test_damage_is_subtracted_from_health(self):
        character = Character()
        character.take_damage(100)
        self.assertEqual(character.health, 900)

    def test_when_damage_received_exceeds_current_health_it_becomes_0(self):
        character = Character()
        character.take_damage(1100)
        self.assertEqual(character.health, 0)

    def test_when_damage_received_exceeds_current_health_die(self):
        character = Character()
        character.take_damage(1100)
        self.assertFalse(character.is_alive())

    def test_dead_characters_cannot_be_healed(self):
        character = Character()
        character.take_damage(1100)
        character.take_heal(800)
        self.assertFalse(character.is_alive())

    def test_healing_cannot_raise_health_above_1000(self):
        character = Character()
        character.take_heal(200)
        self.assertEqual(character.health, 1000)
