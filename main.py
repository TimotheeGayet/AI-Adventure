from srcs import *
import json

def game_loop():

	# Load the save
	save_number = main_menu()

	chat_data = open(f"./saves/chat_data/{save_number}.json", "r").read()
	constant_data = open(f"./saves/constant_data/data{save_number}.json", "r").read()
	chat_data = json.loads(chat_data)
	constant_data = json.loads(constant_data)

	# If the save is empty, start a new game
	if chat_data == "":
		new_game_menu()

	# Main game loop
	while True:
		user_input = get_input("You: ")

		# Get the response from the AI
		response = get_response(user_input, save_number)

		# Update the game data
		chat_data = open(f"./saves/chat_data/{save_number}.json", "r").read()
		constant_data = open(f"./saves/constant_data/data{save_number}.json", "r").read()
		chat_data = json.loads(chat_data)
		constant_data = json.loads(constant_data)

		# Update the inventory and character based on the response
		new_state_of_game = constant_data_update(chat_data[-1]["content"], constant_data['inventory'], constant_data['character_state'])
		open(f"./saves/constant_data/data{save_number}.json", "w").write(new_state_of_game)

		# Print the response
		print(f"Game Master: {response}")

	game_loop()

if __name__ == "__main__":
	game_loop()
