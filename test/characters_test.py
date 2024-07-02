import unittest

from src.character import Character


class CharactersTest(unittest.TestCase):
    def setUp(self):
        self.character1 = Character()
        self.character2 = Character()

    def test_health_starting_at_1000(self):
        self.assertEqual(self.character1.health, 1000)

    def test_level_starting_at_1(self):
        self.assertEqual(self.character1.level, 1)

    def test_starting_alive(self):
        self.assertTrue(self.character1.is_alive())

    def test_damage_is_subtracted_from_health(self):
        self.character1.damage(self.character2, 100)
        self.assertEqual(self.character2.health, 900)

    def test_when_damage_received_exceeds_current_health_it_becomes_0(self):
        self.character1.damage(self.character2, 1100)
        self.assertEqual(self.character2.health, 0)

    def test_when_damage_received_exceeds_current_health_die(self):
        self.character1.damage(self.character2, 1100)
        self.assertFalse(self.character2.is_alive())

    def test_dead_characters_cannot_be_healed(self):
        self.character1.damage(self.character2, 1100)
        self.character2.heal(self.character2, 800)
        self.assertFalse(self.character2.is_alive())

    def test_healing_cannot_raise_health_above_1000(self):
        self.character1.heal(self.character1, 200)
        self.assertEqual(self.character2.health, 1000)

    def test_character_cannot_deal_damage_to_itself(self):
        self.character1.damage(self.character1, 200)
        self.assertEqual(self.character1.health, 1000)

    def test_character_can_heal_itself(self):
        self.character1.damage(self.character2, 200)
        self.character2.heal(self.character2, 100)
        self.assertEqual(self.character2.health, 900)

    def test_damage_is_reduced_by_50_percent_when_target_is_5_or_more_levels_above_the_attacker(self):
        character3 = Character(6)
        self.character1.damage(character3, 100)
        self.assertEqual(character3.health, 950)

    def test_damage_is_increased_by_50_percent_when_target_is_5_or_more_levels_below_the_attacker(self):
        character3 = Character(6)
        character3.damage(self.character1, 100)
        self.assertEqual(self.character1.health, 850)
