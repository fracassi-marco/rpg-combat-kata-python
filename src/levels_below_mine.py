class LevelsBelowMine:
    def __init__(self, attacker, target, threshold: int):
        self.attacker = attacker
        self.target = target
        self.threshold = threshold

    def target_health(self, amount: int):
        return self.target.health - amount * 1.5

    def is_valid(self):
        return self.attacker.level - self.target.level >= self.threshold
