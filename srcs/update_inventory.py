from typing import List
import json

from pydantic import BaseModel
from groq import Groq

groq = Groq()

class Inventory_update_request(BaseModel):
    inventory: List[str]
    character_state: str
    conclusion: str

    @staticmethod
    def model_json_schema():
        return {
            "type": "object",
            "properties": {
                "inventory": {"type": "array", "items": {"type": "string"}},
                "character_state": {"type": "string"},
                "conclusion": {"type": "string"}
            },
            "required": ["inventory", "character_state", "conclusion"],
        }

    @staticmethod
    def model_validate_json(data: dict):
        return Inventory_update_request(**data)

def constant_data_update(situation: str, inventory: List[str], character_state: str):
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an State of Game updater from a video game, you take an inventory, a character and a situation and apply the situation to the inventory and character before sending the answer and a short message describing what happenned to the character_state and his inventory in a nutshell in a JSON object.\n"
                f" The JSON object must use the schema: {json.dumps(Inventory_update_request.model_json_schema(), indent=2)}",
            },
            {
                "role": "user",
                "content": "The situation, inventory and character state are :\n"
                f"- Situation : {situation}\n"
                f"- Inventory : {inventory}\n"
                f"- Character : {character_state}\n",
            },
        ],
        model="llama3-70b-8192",
        temperature=0,
        stream=False,
        response_format={"type": "json_object"},
    )
    
    if Inventory_update_request.model_validate_json(json.loads(chat_completion.choices[0].message.content)):
        return chat_completion.choices[0].message.content
    
    return "error: Invalid JSON object"