class DefaultHeal:
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def target_health(self, amount: int):
        return min(1000, self.target.health + amount)

    def is_valid(self):
        return True
