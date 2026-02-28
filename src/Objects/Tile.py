import src.Engine.GameObject as GameObject
import pygame

class Tile(GameObject.GameObject):
    def __init__(self, width:int, height:int, x:int, y:int, *groups:pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.image.fill((255, 255, 0))

        self.set_position(x, y)