import Items, World
import random


class Player():
	def __init__(self):
		self.inventory = [Items.Rock(), Items.Gold(15), Items.Fists(), Items.Coat()]
		self.equipped = Items.Fists()
		self.equippedDefence = Items.Coat()
		self.hp = 100
		self.location_x, self.location_y = World.starting_position
		self.victory = False

	def is_alive(self):
		return self.hp > 0

	def print_inventory(self):
		i = 1
		for item in self.inventory:
			if hasattr(item, 'damage'):
				print(i, Items.Weapon.__str__(item), '\n')
			elif hasattr(item, 'damageReduction'):
				print(i, Items.Armour.__str__(item), '\n')
			else:
				print(i, Items.Item.__str__(item), '\n')
			i += 1

	def print_equipped(self):
		print('\nCurrent armour: {} \nCurrent weapon {}\n'.format(self.equippedDefence.name, self.equipped.name))

	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy
		print(World.tile_exists(self.location_x, self.location_y).intro_text())

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)

	def equip(self):
		flag = 0
		print('\n')
		for item in self.inventory:
			if hasattr(item, 'damage'):
				print("{}".format(item.name))
		selected = input('equip which weapon?:')
		for item in self.inventory:
			if item.name == selected:
				self.equipped = item
				print("\n{} equipped".format(self.equipped.name))
				flag = 1
				break
		if flag == 0:
			print("You don't have that in your inventory.\n")
		else:
			print("\n")

	def equip2(self):
		flag = 0
		print('\n')
		for item in self.inventory:
			if hasattr(item, 'damageReduction'):
				print("{}".format(item.name))
		selected = input('equip which armour?:')
		for item in self.inventory:
			if item.name == selected:
				self.equipped = item
				print("\n{} equipped".format(self.equipped.name))
				flag = 1
				break
		if flag == 0:
			print("You don't have that in your inventory\n")
		else:
			print("\n")

	def attack(self, enemy):
		print("You attack the {} with your {}.".format(enemy.name, self.equipped.name))
		if self.equipped.damageType == enemy.armour.damageAffinity:
			reduced = (self.equipped.damage - (enemy.armour.damageReduction * 2))
			enemy.hp -= reduced
			print("The {}'s armour seems resistant to your attacks.\n You only dealt {} damage.\n".format(enemy.name, reduced))
			print("The {} has {} HP remaining.".format(enemy.name, enemy.hp))
		if self.equipped.damageType == enemy.armour.damageVulnerability:
			reduced = self.equipped.damage
			enemy.hp -= reduced
			print("the {}'s armour seems to offer little protection from your strikes.\n"
			      "You dealt {} damage.\n".format(enemy.name, reduced))
			print("The {} has {} HP remaining.".format(enemy.name, enemy.hp))
		else:
			reduced = (self.equipped.damage - enemy.armour.damageReduction)
			enemy.hp -= reduced
			print("You dealt {} damage.".format(reduced))
			print("The {} has {} HP remaining.".format(enemy.name, enemy.hp))
		if not enemy.isAlive():
			print("you killed the {}.".format(enemy.name))

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)

	def flee(self, tile):
		"""moves the player to a random available room"""
		available_rooms = tile.adjacent_moves()
		r = random.randint(0, len(available_rooms) - 1)
		self.do_action(available_rooms[r])
