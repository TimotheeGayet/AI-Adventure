import json
from groq import Groq

client = Groq()

def get_response(user_input, save_number):
	with open(f"./saves/chat_data/{save_number}.json", "r") as file:
		data = json.load(file)
	data.append({"role": "user", "content": user_input})
	completion = client.chat.completions.create(
		model="llama3-70b-8192",
		messages=data
	)
	response = completion.choices[0].message.content
	data.append({"role": "system", "content": response})
	json_data = json.dumps(data)
	with open(f"./saves/chat_data/{save_number}.json", "w") as file:
		file.write(json_data)

	return response

