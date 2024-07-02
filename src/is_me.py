class IsMe:
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def target_health(self, amount: int):
        return self.target.health

    def is_valid(self):
        return self.target == self.attacker
