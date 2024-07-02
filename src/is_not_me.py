from src.is_me import IsMe


class IsNotMe:
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def target_health(self, amount: int):
        return self.target.health

    def is_valid(self):
        return not IsMe(self.attacker, self.target).is_valid()
