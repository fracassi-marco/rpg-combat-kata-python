from src.character import Character


class TestCharacters:

    def setup_method(self):
        self.character1 = Character()
        self.character2 = Character()

    def test_health_starting_at_1000(self):
        assert self.character1.health == 1000

    def test_level_starting_at_1(self):
        assert self.character1.level == 1

    def test_starting_alive(self):
        assert self.character1.is_alive() == True

    def test_damage_is_subtracted_from_health(self):
        self.character1.damage(self.character2, 100)
        assert self.character2.health == 900

    def test_when_damage_received_exceeds_current_health_it_becomes_0(self):
        self.character1.damage(self.character2, 1100)
        assert self.character2.health == 0

    def test_when_damage_received_exceeds_current_health_die(self):
        self.character1.damage(self.character2, 1100)
        assert self.character2.is_alive() == False

    def test_dead_characters_cannot_be_healed(self):
        self.character1.damage(self.character2, 1100)
        self.character2.heal(self.character2, 800)
        assert self.character2.is_alive() == False

    def test_healing_cannot_raise_health_above_1000(self):
        self.character1.heal(self.character1, 200)
        assert self.character2.health == 1000

    def test_character_cannot_deal_damage_to_itself(self):
        self.character1.damage(self.character1, 200)
        assert self.character1.health == 1000

    def test_character_can_heal_itself(self):
        self.character1.damage(self.character2, 200)
        self.character2.heal(self.character2, 100)
        assert self.character2.health == 900

    def test_damage_is_reduced_by_50_percent_when_target_is_5_or_more_levels_above_the_attacker(self):
        character3 = Character(6)
        self.character1.damage(character3, 100)
        assert character3.health == 950

    def test_damage_is_increased_by_50_percent_when_target_is_5_or_more_levels_below_the_attacker(self):
        character3 = Character(6)
        character3.damage(self.character1, 100)
        assert self.character1.health == 850

    def test_melee_fighters_have_range_of_2_meters(self):
        character = Character.melee()
        assert character.max_range == 2

    def test_ranged_fighters_have_range_of_20_meters(self):
        character = Character.ranged()
        assert character.max_range == 20

    def test_characters_must_be_in_range_to_deal_damage_to_a_target(self):
        attacker = Character.ranged(position=65)
        target = Character(position=10)
        attacker.damage(target, 100)
        assert target.health == 1000

    def test_allies_cannot_deal_damage_to_one_another(self):
        attacker = Character().joinFaction("foo")
        target = Character().joinFaction("foo")
        attacker.damage(target, 100)
        assert target.health == 1000

    def test_not_allies_can_deal_damage_to_one_another(self):
        attacker = Character().joinFaction("foo")
        target = Character().joinFaction("bar")
        attacker.damage(target, 100)
        assert target.health == 900

    def test_allies_heal_one_another(self):
        attacker = Character(factions=["bar"])
        attacker1 = Character(factions=["foo"])
        target = Character().joinFaction("foo")
        attacker.damage(target, 500)
        attacker1.heal(target, 100)
        assert target.health == 600

    def test_not_allies_cannot_heal_one_another(self):
        attacker = Character(factions=["bar"])
        target = Character().joinFaction("foo")
        attacker.damage(target, 500)
        attacker.heal(target, 100)
        assert target.health == 500
