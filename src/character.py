class Character:

    def __init__(self):
        self.level = 1
        self.health = 1000

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def take_heal(self, amount):
        if not self.is_alive():
            return
        self.health = min(1000, self.health + amount)

