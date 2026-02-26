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

        #are we serious?
        if sprite_num <= 0:
            print("ERROR: Texture: add_sprites: Attempted parse of 0 sprites.")
            return

        try:
            #getting loaded image
            spritesheet = pygame.image.load(src)
        except Exception as e:
            print(f"ERROR: Texture: add_sprites: {e}")
            return
        
        sprite_width = spritesheet.get_width() / sprite_num
        sprite_height = spritesheet.get_height() / sprite_num

        for s in range(sprite_num):
            location_x = sprite_width * s

            sprite = spritesheet.subsurface((location_x, 0), (sprite_width, sprite_height))
            sprite = pygame.transform.scale(sprite, (self.width, self.height))

            self.sprites[f"{sprite_name}{s}"] = sprite       



        