class NotInRange:
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def target_health(self, amount: int):
        return self.target.health

    def is_valid(self):
        return abs(self.target.position - self.attacker.position) > self.attacker.max_range
