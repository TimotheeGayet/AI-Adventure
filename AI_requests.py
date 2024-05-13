import os
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI(
    api_key = dotenv.get("OPENAI_API_KEY")
)


def get_response(user_input, save_number):
	with open(f"./saves/chat_data/{save_number}.json", "r") as file:
		data = json.load(file)
	data.append({"role": "user", "content": user_input})
	completion = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=data
	)
	print(completion.choices[0].message)
	response = completion.choices[0].message
	data.append({"role": "system", "content": response})
	json_data = json.dumps(data)
	with open(f"./saves/chat_data/{save_number}.json", "w") as file:
		file.write(json_data)

	return response

