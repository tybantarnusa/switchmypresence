from dotenv import load_dotenv
from operator import itemgetter
import os
import json

class Games:
    def __init__(self):
        pass

    def get_list(self):
        json_file = None

        try:
            json_path = 'gamelist.json'
            json_file = open(json_path)
        except:
            try:
                json_path = os.path.join(os.path.dirname(__file__), '../assets/' + json_path)
                json_file = open(json_path)
            except Exception as e:
                raise e
                
        game_data = json.load(json_file)

        return sorted(game_data['games'], key=itemgetter('title'))

instance = Games()