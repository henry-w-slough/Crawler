from src.Engine import Screen
import src.Map.Map as Map
import src.Objects.Tile as Tile
import pygame


class MapLoader():
    def __init__(self) -> None:
        
        self.maps = {

        }


    def load_map(self, src:str, name:str) -> Map.Map:
        #creating the new Map object, which holds all the data from the src json
        new_map = Map.Map(src)
        #adding to dict of maps
        self.maps[name] = new_map
        return new_map
    

    def get_map(self, name:str) -> Map.Map:
        return self.maps[name]
    
    
    def map_to_group(self, group:pygame.sprite.Group, map_name:str) -> None:

        #getting data references
        map = self.get_map(map_name)
        data = map.level_data

        for layer in data["layers"]:

            for index, tile_id in enumerate(layer["data"]):

                if tile_id != 0:

                    x = (index % layer["width"]) * (data["tilewidth"])
                    y = (index // layer["width"]) * (data["tileheight"])

                    Tile.Tile(data["tilewidth"], data["tileheight"], x, y, group)

        
    
    