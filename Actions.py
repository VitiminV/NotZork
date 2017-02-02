from Player import Player


class Action():
	def __init__(self, method, name, hotkey, **kwargs):
		self.method = method
		self.name = name
		self.hotkey = hotkey
		self.kwargs = kwargs

	def __str__(self):
		return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
	def __init__(self):
		super().__init__(method=Player.move_north, name='Move north', hotkey='n')


class MoveSouth(Action):
	def __init__(self):
		super().__init__(method=Player.move_south, name='Move south', hotkey='s')


class MoveEast(Action):
	def __init__(self):
		super().__init__(method=Player.move_east, name='Move east', hotkey='e')


class MoveWest(Action):
	def __init__(self):
		super().__init__(method=Player.move_west, name='Move west', hotkey='w')


class ViewInventory(Action):
	"""Prints the current inventory"""

	def __init__(self):
		super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')


class Attack(Action):
	"""Attacks the selected enemy"""

	def __init__(self, enemy):
		super().__init__(method=Player.attack, name='Attack', hotkey='a', enemy=enemy)


class Flee(Action):
	"""Moves the player randomly to an adjacent tile"""

	def __init__(self, tile):
		super().__init__(method=Player.flee, name='Flee', hotkey='f', tile=tile)


class Equip(Action):
	"""Equips selected weapon"""

	def __init__(self):
		super().__init__(method=Player.equip, name='Equip', hotkey='q')


class Equip2(Action):
	def __init__(self):
		super().__init__(method=Player.equip2, name='Equip Armour', hotkey='l')


class ViewEquipped(Action):
	def __init__(self):
		super().__init__(method=Player.print_equipped, name='View equipped', hotkey='r')

class Die(Action):
	def __init__(self):
		super().__init__(method=Player.die, name='die', hotkey='')

class DieToTrap(Action):
	def __init__(self):
		super().__init__(method=Player.die, name='die to trap', hotkey='')