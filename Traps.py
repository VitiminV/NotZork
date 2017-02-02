import Player,Items,Tiles

class Trap:
	def __init__(self, name, description, damage, key):
		self.name = name
		self.description = description
		self.damage = damage
		self.key = key

class pit_bridge(Trap):
	def __init__(self):
		super().__init__(name="Narrow Bridge trap",
		                 description="TODO: HAVE GIRLFRIEND WRITE",
		                 damage=999999999999999,
		                 key=Items.Torch)