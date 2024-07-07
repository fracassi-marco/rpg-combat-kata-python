from src.default_heal import DefaultHeal
from src.same_faction import SameFaction


class IsAllie:
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def target_health(self, amount: int):
        return DefaultHeal(self.attacker, self.target).target_health(amount)

    def is_valid(self):
        return SameFaction(self.attacker, self.target).is_valid()
