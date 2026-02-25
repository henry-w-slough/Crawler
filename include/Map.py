import json


class Map():
    def __init__(self, src:str) -> None:

        self.level_data = ""

        #loading the map, if it can't be loaded the level_data is just empty
        try:
            self.level_data = json.load(src)
        except Exception as e:
            print(f"ERROR: Map: Init: {e}")

        