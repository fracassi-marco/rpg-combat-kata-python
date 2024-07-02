class Character:

    def __init__(self, level: int = 1):
        self.level = level
        self.health = 1000

    def is_alive(self):
        return self.health > 0

    def damage(self, target, amount: int):
        if self.__is_me(target):
            return
        if self.__levels_above_mine(target) >= 5:
            amount = amount * 0.5
        if self.__levels_below_mine(target) >= 5:
            amount = amount * 1.5
        target.health = max(0, target.health - amount)

    def heal(self, target, amount: int):
        if not target.is_alive():
            return
        if not self.__is_me:
            return
        target.health = min(1000, target.health + amount)

    def __is_me(self, target):
        return target == self

    def __levels_above_mine(self, target):
        return target.level - self.level

    def __levels_below_mine(self, target):
        return self.level - target.level
