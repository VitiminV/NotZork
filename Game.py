import World, Player, Tiles, Traps, Actions
from Player import Player


def play():
	# Load the world, create a player, initialize player to the starting room, and display text
	World.load_tiles()
	player = Player()
	room = World.tile_exists(player.location_x, player.location_y)
	print(room.intro_text())
	# Initialize game loop
	while True:
		if player.is_alive() and not player.victory():
			print("choose an action:\n")
			available_actions = room.available_actions()
			for action in available_actions:
				print(action)
			action_input = input("Action: ")
			previous_input = 'n'
			if room.tile_name == 'PitBridge' and (action_input != previous_input or action_input == 'i' or
													action_input == 'q' or action_input == 'l' or action_input == 'r'):
				player.do_action(Actions.DieToTrap())
				break
			else:
				player.do














"""while player.is_alive() and not player.victory:
		# Loop begins Here
		room = World.tile_exists(player.location_x, player.location_y)
		room.modify_player(player)
		# Check health and victory state
		if player.is_alive() and not player.victory:
			print("Choose an action:\n")
			available_actions = room.available_actions()
			for action in available_actions:
				print(action)
			action_input = input('Action: ')
			for action in available_actions:
				if action_input == action.hotkey:
					player.do_action(action, **action.kwargs)
					break"""


if __name__ == '__main__':
	play()
