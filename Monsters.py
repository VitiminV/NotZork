class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def isAlive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider",
                         hp=10,
                         damage=2)


class Cultist(Enemy):
    def __init__(self):
        super().__init__(name="Cultist",
                         hp=30,
                         damage=15)