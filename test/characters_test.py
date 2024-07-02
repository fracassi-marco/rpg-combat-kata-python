import unittest

from src.character import Character


class CharactersTest(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.character = Character()

    def test_health_starting_at_1000(self):
        self.assertEqual(self.character.health, 1000)

    def test_level_starting_at_1(self):
        self.assertEqual(self.character.level, 1)

    def test_starting_alive(self):
        self.assertTrue(self.character.is_alive())

    def test_damage_is_subtracted_from_health(self):
        self.character.take_damage(100)
        self.assertEqual(self.character.health, 900)

    def test_when_damage_received_exceeds_current_health_it_becomes_0(self):
        self.character.take_damage(1100)
        self.assertEqual(self.character.health, 0)

    def test_when_damage_received_exceeds_current_health_die(self):
        self.character.take_damage(1100)
        self.assertFalse(self.character.is_alive())

    def test_dead_characters_cannot_be_healed(self):
        self.character.take_damage(1100)
        self.character.take_heal(800)
        self.assertFalse(self.character.is_alive())

    def test_healing_cannot_raise_health_above_1000(self):
        self.character.take_heal(200)
        self.assertEqual(self.character.health, 1000)
