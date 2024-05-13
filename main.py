from AI_requests import *
from menu import *

def game_loop():

	# Load the save
	save_number = main_menu()

	# If the save is empty, start a new game
	if open(f"./saves/chat_data/{save_number}.json", "r").read() == "":
		new_game(save_number)

	# Main game loop
	while True:
		user_input = get_input("You: ")

		# Get the response from the AI
		response = get_response(user_input, save_number)

		# Print the response
		print(f"Game Master: {response}")

	game_loop()

if __name__ == "__main__":
	game_loop()
