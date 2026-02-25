import pygame


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
        

    def add_sprites(self, src:str, sprite_width:int, sprite_height:int, sprite_name:str) -> None:

        try:
            #returning loaded image scaled to the texture size
            spritesheet = pygame.image.load(src)
        except Exception as e:
            #fallback surface for invalid src arg
            print(f"ERROR: Texture: add_sprites: {e}")
            return

        #this assumes spritesheets have 1 row and are made horizontal... Yikes!
        total_sprites = spritesheet.get_width()//sprite_width
        
        for s in range(total_sprites):
            #getting the sprite portion of the sheet
            sprite = spritesheet.subsurface(pygame.Rect(sprite_width*s, 0, sprite_width, sprite_height))
            #resizing the new sprite
            sprite = pygame.transform.scale(sprite, (self.width, self.height))
            
            self.sprites[f"{sprite_name}{s}"] = sprite
        



        