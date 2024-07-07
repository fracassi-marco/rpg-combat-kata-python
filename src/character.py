from src.default_damage import DefaultDamage
from src.default_heal import DefaultHeal
from src.is_dead import IsDead
from src.is_me import IsMe
from src.is_not_me import IsNotMe
from src.levels_above_mine import LevelsAboveMine
from src.levels_below_mine import LevelsBelowMine
from src.not_in_range import NotInRange
from src.same_faction import SameFaction


class Character:

    @classmethod
    def melee(cls, position: int = 1000):
        return Character(max_range=2, position=position)

    @classmethod
    def ranged(cls, position: int = 1000):
        return Character(max_range=20, position=position)

    def __init__(self, level: int = 1, max_range: int = 1000, position: int = 1000, factions=None):
        self.level = level
        self.max_range = max_range
        self.health = 1000
        self.position = position
        self.factions = factions or []

    def is_alive(self):
        return self.health > 0

    def damage(self, target, amount: int):
        rules = [NotInRange(self, target),
                 IsMe(self, target),
                 SameFaction(self, target),
                 LevelsAboveMine(self, target, 5),
                 LevelsBelowMine(self, target, 5),
                 DefaultDamage(self, target)]
        self.__apply_first(amount, rules, target)

    def heal(self, target, amount: int):
        rules = [IsDead(self, target),
                 IsNotMe(self, target),
                 DefaultHeal(self, target)]
        self.__apply_first(amount, rules, target)

    def __apply_first(self, amount, rules, target):
        for rule in rules:
            if rule.is_valid():
                target.health = rule.target_health(amount)
                break

    def joinFaction(self, faction):
        return Character(level=self.level, max_range=self.max_range, position=self.position, factions=self.factions + [faction])
