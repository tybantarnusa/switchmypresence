from dotenv import load_dotenv
from operator import itemgetter
import os
import json

class Games:
    def __init__(self):
        pass

    def get_list(self):
        load_dotenv()

        env = os.environ.get("ENV")

        json_path = 'gamelist.json'
        if env == 'development':
           json_path = os.path.join(os.path.dirname(__file__), '../assets/' + json_path)

        json_file = open(json_path)
        game_data = json.load(json_file)

        return sorted(game_data['games'], key=itemgetter('title'))

instance = Games()