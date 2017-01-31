"""I don't know why I have to import all these separately.
   'from asciimatics import *' doesn't work."""
from asciimatics import widgets
from asciimatics import effects
from asciimatics import screen
from asciimatics import event
from asciimatics import exceptions
from asciimatics import particles
from asciimatics import paths
from asciimatics import renderers
from asciimatics import scene
from asciimatics import sprites
from asciimatics import version
import Player,World,Tiles,Actions


class Map(widgets.Frame):
	def __init__(self, screen, model):
		super(Map, self).__init__(
			screen,
			screen.height * 2 // 3,
			screen.width * 2 // 3,
			on_load=self._reload_map,
			hover_focus=True,
			title="Map")
		self._model = model
		frame = widgets.Frame(screen, 57, 98, has_border=True)
		display_layout = widgets.Layout([100], fill_frame=False)
		frame.add_layout(display_layout)
		width, height = World.get_dimensions()
		for x in width:
			for y in height:
				self.draw_room()

	def draw_room(self, tile):
		moves = tile.adjacent_moves()
		if moves == [Actions.MoveSouth(), Actions.MoveNorth(), Actions.MoveEast(), Actions.MoveWest()]:
			return """┏━━━┛ ┗━━━┓
			           ┃          ┃
			           ┃          ┃
			           ┛          ┗
			           ┓          ┏
			           ┃          ┃
			           ┃          ┃
			           ┗━━━┓ ┏━━━┛"""
		if moves == [Actions.MoveSouth(), Actions.MoveNorth(), Actions.MoveEast()]:
			return """┏━━━┛ ┗━━━┓
					   ┃          ┃
			           ┃          ┃
					   ┃          ┗
					   ┃          ┏
					   ┃          ┃
					   ┃          ┃
					   ┗━━━┓ ┏━━━┛"""
		if moves == [Actions.MoveSouth(), Actions.MoveNorth(), Actions.MoveWest()]:
			return """┏━━━┛ ┗━━━┓
					   ┃          ┃
					   ┃          ┃
			     	   ┛          ┃
					   ┓          ┃
					   ┃          ┃
					   ┃          ┃
					   ┗━━━┓ ┏━━━┛"""