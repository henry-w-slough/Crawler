from include.Engine import Screen
import include.Map.Map as Map
import include.Objects.Tile as Tile
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
        map = self.get_map(map_name)
        data = map.level_data

        t_w = data["tilewidth"]
        t_h = data["tileheight"]

        #forgive me father for I have sinned
        for x, row in enumerate(data["layers"][0]["data"]):
            for y, column in enumerate(data["layers"][0]["data"]):
                Tile.Tile(t_w, t_h, x*t_w, y*t_h, group)

        
    
    