import json
from time import sleep

def get_input(str):
	try:
		return input(str)
	except KeyboardInterrupt:
		print("\nQuitting!")
		exit()

def init_game_data(save_number):
	# Define the starting data for the game
	starting_chat_data = [
		{"role": "system", "content": "You are a roleplay game master / storyteller following the player choices to create an adventure. Never forget to give vivid descriptions and make the player feel like they are in the game world !"},
	]
	constant_data_starting = {
		"inventory": [],
		"character_state": "The adventurer is full life and full energy.",
		"conclusion": "You have started your adventure"
	}

	# Convert the data to JSON format
	json_chat_data = json.dumps(starting_chat_data)
	json_constant_data = json.dumps(constant_data_starting)

	# Write the JSON data to the file
	with open(f"./saves/chat_data/{save_number}.json", "w") as file:
		file.write(json_chat_data)
	with open(f"./saves/constant_data/data{save_number}.json", "w") as file:
		file.write(json_constant_data)

	print(f"Game data initialized for save {save_number}!")


def new_game_menu(save_number = 0):
	print("Starting a new game!\n")
	sleep(0.5)
	print("Select the save you wish to overwrite!")
	print("** Please note that this action is irreversible and will erase all previous data ! **\n")

	if save_number > 0:
		init_game_data(save_number)

	for i in range(1, 4):
		if open(f"./saves/chat_data/{i}.json", "r").read() == "":
			print(f"{i}. Save {i} (Empty)")
		else:
			print(f"{i}. Save {i} (Occupied)\n")

	choice = input("Enter the number of your choice: ")
	if choice in ["1", "2", "3"]:
		init_game_data(int(choice))
		return int(choice)
	else:
		print("Invalid choice!")
		return main_menu()


def main_menu():
	print("Welcome to the game!")
	print("1. Start a new game")
	print("2. Load a saved game")
	print("3. Quit\n")
	choice = get_input("Enter the number of your choice: ")
	if choice == "1":
		return new_game_menu()
	elif choice == "2":
		print("Loading a saved game!\n")
		save_number = get_input("Enter the save number: ")
		return int(save_number) if save_number in ["1", "2", "3"] else print("Invalid save number!")
	elif choice == "3":
		print("Quitting!")
		exit()
	else:
		print("Invalid choice!")
	main_menu()
