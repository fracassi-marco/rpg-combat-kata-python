class LevelsAboveMine:
    def __init__(self, attacker, target, threshold: int):
        self.attacker = attacker
        self.target = target
        self.threshold = threshold

    def target_health(self, amount: int):
        return self.target.health - amount * 0.5

    def is_valid(self):
        return self.target.level - self.attacker.level >= self.threshold