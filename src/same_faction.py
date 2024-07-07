class SameFaction:
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def target_health(self, amount: int):
        return self.target.health

    def is_valid(self):
        return len(set(self.target.factions).intersection(self.attacker.factions)) > 0
