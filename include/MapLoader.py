import json
import include.Map as Map


class MapLoader():
    def __init__(self) -> None:
        pass

    def load_map(self, src:str) -> Map.Map:
        return Map.Map(src)
        
    
    