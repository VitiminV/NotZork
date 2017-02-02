import Items


class Enemy:
    def __init__(self, name, hp, weapon, armour):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armour = armour

    def isAlive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider",
                         hp=10,
                         weapon=Items.SpiderFang(),
                         armour=Items.ExoSkeleton())


class Cultist(Enemy):
    def __init__(self):
        super().__init__(name="Cultist",
                         hp=30,
                         weapon=Items.CultistDagger(),
                         armour=Items.CultistsRobes())


class Shoggoth(Enemy):
	def __init__(self):
		super().__init__(name="Shoggoth",
		                 hp=60,
		                 weapon=Items.ShoggothTentacle(),
		                 armour=Items.NoArmour())


class Chort(Enemy):
	def __init__(self):
		super().__init__(name="Chort",
		                 hp=40,
		                 weapon=Items.ChortWhip(),
		                 armour=Items.NoArmour())
