import Items, Monsters, Actions, World, Traps
from Player import Player


class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def adjacent_moves(self):
		"""returns all move actions for adjacent tiles"""
		moves = []
		if World.tile_exists(self.x + 1, self.y):
			moves.append(Actions.MoveEast())
		if World.tile_exists(self.x - 1, self.y):
			moves.append(Actions.MoveWest())
		if World.tile_exists(self.x, self.y - 1):
			moves.append(Actions.MoveNorth())
		if World.tile_exists(self.x, self.y + 1):
			moves.append(Actions.MoveSouth())
		return moves

	def available_actions(self):
		"""returns all of the available actions in this room"""
		moves = self.adjacent_moves()
		moves.append(Actions.ViewInventory())
		moves.append(Actions.Equip())
		moves.append(Actions.Equip2())
		moves.append(Actions.ViewEquipped())
		return moves


def intro_text(self):
	raise NotImplementedError()


def modify_player(self, player):
	raise NotImplementedError()


class StartingRoom(MapTile):
	def intro_text(self):
		return """You Find yourself in a dark library. The dim glow of the emergency lights cast long, foreboding
		 shadows on the books around you. You don't remember where you are, but you remember that you are in grave
		 danger. You hear a terrible, inhuman groaning and wretching coming from deep within the facility, and an
		 indescribable sense of dread chills you to the core. You see 4 possible paths forward, choose one, and begin
		 your escape."""

	def modify_player(self, player):
		"""room has no effect on player"""
		pass


class LootRoom(MapTile):
	looted = 0

	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)

	def add_loot(self, player):
		player.inventory.append(self.item)
		self.looted = 1

	def modify_player(self, player):
		self.add_loot(player)

	def been_looted(self):
		return self.looted == 1


class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)

	def modify_player(self, player):
		if self.enemy.isAlive():
			if player.equippedDefence.damageAffinity == self.enemy.weapon.damageType:
				reduced = self.enemy.weapon.damage - (player.equippedDefence.damageReduction * 2)
				player.hp -= reduced
				print("Enemies strike seems to have been softened by your armour. It only does {} damage. \n"
				      "You have {} HP remaining.\n".format(reduced, player.hp))
			else:
				reduced = self.enemy.weapon.damage - player.equippedDefence.damageReduction
				player.hp -= reduced
			print("Enemy does {} damage. You have {} HP remaining.\n".format(reduced, player.hp))

	def adjacent_moves(self):
		"""returns all move actions for adjacent tiles"""
		moves = []
		if World.tile_exists(self.x + 1, self.y):
			moves.append(Actions.MoveEast())
		if World.tile_exists(self.x - 1, self.y):
			moves.append(Actions.MoveWest())
		if World.tile_exists(self.x, self.y - 1):
			moves.append(Actions.MoveNorth())
		if World.tile_exists(self.x, self.y + 1):
			moves.append(Actions.MoveSouth())
		return moves

	def available_actions(self):
		if self.enemy.isAlive():
			return [Actions.Flee(tile=self), Actions.Attack(enemy=self.enemy)]
		else:
			return MapTile.available_actions(self)


class TrapRoom(MapTile):

	def __init__(self, x, y, trap):
		self.trap = trap
		super().__init__(x, y)




class EmptyRoom(MapTile):
	def intro_text(self):
		return """The walls and bookshelves stare silently back at you. This room is mercifully, empty."""

	def modify_player(self, player):
		"""room has no effect on player"""
		pass



class GiantSpiderRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Monsters.GiantSpider())

	def intro_text(self):
		if self.enemy.isAlive():
			return """As you enter the room, you see a massive, hairy spider. As it stands up to look at you, you
			realize it's almost as tall as you are. It bears its fangs as it prepares to fight."""
		else:
			return """The dead spider (thankfully) lies motionless where it fell."""


class CultistRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Monsters.Cultist())

	def intro_text(self):
		if self.enemy.isAlive():
			return """The ramblings of the madman cause your head to pound. You stumble, and catch his attention.
			As you lock bloodshot eyes with him, you notice a wild, sinister grin spread across his face before
			he attacks."""
		else:
			return """The now lifeless eyes of the once crazed cultist now stare blankly into space."""


class ChortRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Monsters.Chort())

	def intro_text(self):
		if self.enemy.isAlive():
			return """A rancid and sour smell permeates the air. In the corner of the room,
			you hear an arrhythmic snorting and wheezing. An abomination stepped from the shadows, the light revealing
			a tall emaciated figure with a hairless boar head.Uneven horns grew out of weeping soars, with pus crusted
			down the creatures skull.The lashing, pronged tail reminded you of a common folk myth,
			a chort, devil of fairs. With a squeal, it raised a three-pronged whip and charges."""
		else:
			return """Viscous foam and blood flecks the creatures mouth. Evidence of it's last wheezing squeal."""


class FindKnifeRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Items.Knife())

	def intro_text(self):
		if self.looted == 0:
			return """The light catches on a piece of metal, and you notice a small kitchen knife embedded in the wall.
			You pick it up. It's not much, but it makes you feel a little better."""
		else:
			return """The hole in the wall reminds you of where the knife used to be."""


class FindGoldRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Items.Gold(10))

	def intro_text(self):
		if self.looted == 0:
			return """A soft yellow glimmer catches your eye, and you notice a small pile of gold coins strewn across the
			top of a nearby desk."""
		else:
			return """The desk is looking remarkably unremarkable without the loot it once held."""


class FindM1911Room(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Items.M1911())

	def intro_text(self):
		return """Upon entering the room, you quickly notice a corpse. As you move to investigate, you can see large
		wounds either sides of his head. You look down and notice a gun in his left hand. You suppose he won't mind,
		as you need it more than he does. As you touch it, An alien chanting fills your ears, and you grab your head in
		agony. The feeling quickly subsides, and as you regain composure, fleeting glimpses of alien architecture and
		impossible geometry fade from your mind."""


class ExitRoom(MapTile):
	def intro_text(self):
		return """A bright red light catches your eye as you enter the room. It's an exit sign! You carefully make your
		way over to it, and push on the handle. It wont budge. You notice the sticker on the door that reads 'PULL', and
		give the door a tug. It opens! The cool night air fills your lungs and you take off sprinting into the night,
		 your every footfall putting a little more distance between you and that mad house. You're free."""

	def modify_player(self, player):
		player.victory = True
