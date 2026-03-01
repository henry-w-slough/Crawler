import src.Objects.Tile as Tile
import pygame
import json


class MapLoader():
    def __init__(self) -> None:
        """Loads all maps passed with load_map() and holds them in a dict for access."""
        
        self.maps = {

        }


    def load_map(self, src:str, name:str) -> None:
        """Adds a new Map to the MapLoader's maps dict. (Name, Data) for map dictionary."""
        #adding all the map data from the json file and excepting error
        try:
            with open(src, "r") as map_json:
                self.maps[name] = json.load(map_json)
        except Exception as e:
            print(f"ERROR: MapLoader: load_map: {e}")
    

    def get_map_data(self, name:str) -> dict:
        """Returns data dict of map data corresponding to given name in MapLoader map dict."""
        try:
            return self.maps[name]
        except Exception as e:
            print(f"ERROR: MapLoader: get_map: {e}")
            return {}
    
    
    def map_to_group(self, group:pygame.sprite.Group, map_name:str) -> None:
        """Translates Map object with map_name's json data to Tile class objects and adds them to the given pygame.sprite.Group to be drawn and updated."""
        #getting data references
        data = self.get_map_data(map_name)

        for layer in data["layers"]:

            for index, tile_id in enumerate(layer["data"]):
                
                x = (index % layer["width"]) * (data["tilewidth"])
                y = (index // layer["width"]) * (data["tileheight"])

                if tile_id == 1:
                    Tile.Brick(data["tilewidth"], data["tileheight"], x, y, group)
                if tile_id == 2:
                    Tile.Wood(data["tilewidth"], data["tileheight"], x, y, group)

        
    
    