class Item():
    """The Base Class for all the loot and magical nonsense"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):
    """A very unfortunate schmelting accident..."""
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round gold coin with a faded figure, and some alien symbols "
                                      "stamped on both sides.",
                         value=self.amt)


class Weapon(Item):
    """The Base Class for all the pointy Sticks"""
    def __init__(self, name, description, value, damage, damageType):
        self.damage = damage
        self.damageType = damageType
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\nDamage Type: {}".format(self.name, self.description, self.value,
                                                                              self.damage, self.damageType)


class Armour(Item):
    """Something between you and the swords"""
    def __init__(self, name, description, value, damageReduction, damageAffinity, damageVulnerability):
        self.damageReduction = damageReduction
        self.damageAffinity = damageAffinity
        self.damageVulnerability = damageVulnerability
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage Reduction: {}\nDamage Type: {}".format(self.name, self.description, self.value,
                                                                              self.damageReduction, self.damageAffinity)


class Rock(Weapon):
    """and roll"""
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5,
                         damageType='Bludgeoning')


class Knife(Weapon):
    """Whats a dungeon crawler without pointy objects?"""
    def __init__(self):
        super().__init__(name="Knife",
                         description="A small, cheap kitchen knife. Barely more effective than a rock.",
                         value=10,
                         damage=10,
                         damageType='Piercing')


class M1911(Weapon):
    """.45 ACP > 9mm. fite me /k/."""
    def __init__(self):
        super().__init__(name="M1911",
                         description="An old reliable sidearm. Strange, the magazine seems stuck, but the gun seems to"
                                     "function anyway. There are some strange symbols etched onto the slide. You can't"
                                     "understand them, but the world 'bottomless' floats through your mind upon reading"
                                     "them",
                         value=50,
                         damage=18,
                         damageType='Ballistic')


class Fists(Weapon):
    """Good 'ol rightie and leftie"""
    def __init__(self):
        super().__init__(name="Fists",
                         description="Your balled up hands attached to the ends of your arms",
                         value=0,
                         damage=2,
                         damageType='Bludgeoning')


class Coat(Armour):
    """If its a trench-coat, you're a neckbeard"""
    def __init__(self):
        super().__init__(name="Coat",
                         description="It's your old overcoat. It's familiarity provides some comfort.",
                         value=5,
                         damageReduction=1,
                         damageAffinity='Bludgeoning',
                         damageVulnerability='None')

class SpiderFang(Weapon):
    """shelob"""
    def __init__(self):
        super().__init__(name="Spider Fang",
                         description="You Shouldn't be seeing this in game. pls leme know on github.",
                         value=0,
                         damage=2,
                         damageType='Piercing')

class CultistDagger(Weapon):
    """Draw the lines... Cut the man... Drain the blood..."""
    def __init__(self):
        super().__init__(name="Cultist Dagger",
                         description="You Shouldn't be seeing this in game. pls leme know on github.",
                         value=0,
                         damage=8,
                         damageType='Piercing')

class ExoSkeleton(Armour):
    """fookin boogs"""
    def __init__(self):
        super().__init__(name="Exo Skeleton",
                         description="You Shouldn't be seeing this in game. pls leme know on github.",
                         value=0,
                         damageReduction=2,
                         damageAffinity='Magic',
                         damageVulnerability='Bludgeoning')


class CultistsRobes(Armour):
    """Spooky Magic Robes"""
    def __init__(self):
        super().__init__(name="CultistsRobes",
                         description="You Shouldn't be seeing this in game. pls leme know on github.",
                         value=0,
                         damageReduction=2,
                         damageAffinity='Magic',
                         damageVulnerability='Piercing')
