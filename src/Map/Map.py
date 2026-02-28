import json


class Map():
    def __init__(self, src:str) -> None:

        self.level_data = {

        }

        #adding all the map data from the json file and excepting error
        try:
            with open(src, "r") as map_json:
                self.level_data = json.load(map_json)
        except Exception as e:
            print(f"ERROR: Map:  __init__: {e}")

        