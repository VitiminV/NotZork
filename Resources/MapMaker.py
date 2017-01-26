import World, Player, Tiles
from Player import Player

World.load_tiles()

class MapPart():
	def __init__(self, name, data, numberOfDoors):
		self.name = name
		self.data = data
		self.numberOfDoors = numberOfDoors

	def room_selector(self):
		dims = World.get_dimensions()
		width = dims[0]
		height = dims[1]
		for x in width

	def draw_room(self, tile):
		if
