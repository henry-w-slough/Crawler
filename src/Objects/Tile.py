from pygame.sprite import Group

import src.Engine.GameObject as GameObject
import pygame

class Tile(GameObject.GameObject):
    def __init__(self, width:int, height:int, x:int, y:int, *groups:pygame.sprite.Group) -> None:
        """GameObject that represents a Tile on the 'ground', passes in x and y values for placement."""
        super().__init__(width, height, *groups)

        self.set_position(x, y)

        self.texture.add_sprites("assets/spritesheets/tilemap.png", 4, "tile")


class Brick(Tile):
    def __init__(self, width: int, height: int, x: int, y: int, *groups: Group) -> None:
        super().__init__(width, height, x, y, *groups)
        
        self.image = self.texture.get_sprite("tile0")


class Wood(Tile):
    def __init__(self, width: int, height: int, x: int, y: int, *groups: Group) -> None:
        super().__init__(width, height, x, y, *groups)
        
        self.image = self.texture.get_sprite("tile1")

