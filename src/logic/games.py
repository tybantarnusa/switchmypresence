from operator import itemgetter
from logic import util
import os
import json


class Games:
    def __init__(self):
        pass

    def get_list(self):
        json_file = None

        try:
            json_path = util.resource_path('gamelist.json')
            json_file = open(json_path)
        except:
            try:
                json_path = util.resource_path('../assets/gamelist.json')
                json_file = open(json_path)
            except Exception as e:
                raise e
                
        game_data = json.load(json_file)

        return sorted(game_data['games'], key=itemgetter('title'))

instance = Games()