import json
import os
import random


class JsonLoader:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_CONTENT = ""

    def __init__(self, file_name):
        self.file_name = file_name
        self.fetch_content()
        
    def fetch_content(self):
        try:
            json_path = os.path.join(self.BASE_DIR, "resources", f"{self.file_name}.json")

            with open(json_path, mode="r", encoding="utf-8") as json_file:
                self.JSON_CONTENT = json.load(json_file)
        except Exception as e:
            print(f"Error attempting to load {self.file_name} : {e}")

    def get_random(self, theme):
        return random.choice(self.JSON_CONTENT[theme])


class MPSender:
    def return_sender_from_obj(obj):
        if obj.__class__.__name__ == "Member":
            return obj
        elif obj.__class__.__name__ == "Message":
            return obj.author
        elif obj.__class__.__name__ == "Context":
            return obj.message.author
        else:
            return None

    async def send_mp(obj, msg):
        recipient = MPSender.return_sender_from_obj(obj)
        try:
            await recipient.send(msg)
        except Exception as e:
            print(f"Failed to send MP (recipient {recipient}): {e}")