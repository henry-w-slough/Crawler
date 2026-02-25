import pygame
import math


class Texture():
    def __init__(self, width:int, height:int) -> None:
        
        self.width = width
        self.height = height

        #holds all sprites added through spritesheets
        self.sprites = {

        }


    def get_sprite(self, name:str) -> pygame.Surface:
        #returns the corresponding sprite in the object's sprites dict
        return self.sprites.get(name, pygame.Surface((self.width, self.height)))
        

    def add_sprites(self, src:str, sprite_num:int, sprite_name:str) -> None:

        try:
            #returning loaded image scaled to the texture size
            spritesheet = pygame.image.load(src)
        except Exception as e:
            #fallback surface for invalid src arg
            print(f"ERROR: Texture: add_sprites: {e}")
            return
        
        sprite_width = spritesheet.get_width() / sprite_num
        sprite_height = spritesheet.get_height() / sprite_num

        for s in range(sprite_num):
            location_x = sprite_width * s

            sprite = spritesheet.subsurface((location_x, 0), (sprite_width, sprite_height))
            sprite = pygame.transform.scale(sprite, (self.width, self.height))

            self.sprites[f"{sprite_name}{s}"] = sprite       



        