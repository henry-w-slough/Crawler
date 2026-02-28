import pygame


class Texture():
    def __init__(self, width:int, height:int) -> None:
        """Class to hold all animations and images needed for an object on the screen. Width and Height are both the size of one sprite."""
        
        self.width = width
        self.height = height

        #holds all sprites added through spritesheets
        self.sprites = {

        }


    def get_sprite(self, name:str) -> pygame.Surface:
        """Returns the sprite by given name in the object's sprites dict."""
        #returns the corresponding sprite in the object's sprites dict
        return self.sprites.get(name, pygame.Surface((self.width, self.height)))
        

    def add_sprites(self, src:str, sprite_num:int, sprite_name:str) -> None:
        """Adds sprites from the given spritesheet source."""

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
        
        #iterating through all calculated sprites
        for s in range(sprite_num):
            #getting x pos, assumes spritesheets are horizontal
            location_x = self.width * s

            #cutting the sprite and transforming it to the scale of the texture
            sprite = spritesheet.subsurface((location_x, 0), (self.width, self.height))
            sprite = pygame.transform.scale(sprite, (self.width, self.height))

            #adding
            self.sprites[f"{sprite_name}{s}"] = sprite       



        