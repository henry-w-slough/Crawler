import src.Map.Map as Map
import src.Objects.Tile as Tile
import pygame


class MapLoader():
    def __init__(self) -> None:
        """Loads all maps passed with load_map() and holds them in a dict for access."""
        
        self.maps = {

        }


    def load_map(self, src:str, name:str) -> Map.Map:
        """Adds a new Map object to the MapLoader's maps dict. Passes json src to new Map with given name."""
        #creating the new Map object, which holds all the data from the src json
        new_map = Map.Map(src)
        #adding to dict of maps
        self.maps[name] = new_map
        return new_map
    

    def get_map(self, name:str) -> Map.Map:
        """Returns the map of given name in maps dict."""
        return self.maps[name]
    
    
    def map_to_group(self, group:pygame.sprite.Group, map_name:str) -> None:
        """Translates Map object with map_name's json data to Tile class objects and adds them to the given pygame.sprite.Group to be drawn and updated."""
        #getting data references
        map = self.get_map(map_name)
        data = map.level_data

        for layer in data["layers"]:

            for index, tile_id in enumerate(layer["data"]):
                
                x = (index % layer["width"]) * (data["tilewidth"])
                y = (index // layer["width"]) * (data["tileheight"])

                if tile_id == 1:
                    Tile.Brick(data["tilewidth"], data["tileheight"], x, y, group)
                if tile_id == 2:
                    Tile.Wood(data["tilewidth"], data["tileheight"], x, y, group)

        
    
    