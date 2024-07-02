from src.default_damage import DefaultDamage
from src.default_heal import DefaultHeal
from src.is_dead import IsDead
from src.is_me import IsMe
from src.is_not_me import IsNotMe
from src.levels_above_mine import LevelsAboveMine
from src.levels_below_mine import LevelsBelowMine


class Character:

    def __init__(self, level: int = 1):
        self.level = level
        self.health = 1000

    def is_alive(self):
        return self.health > 0

    def damage(self, target, amount: int):
        rules = [IsMe(self, target),
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
