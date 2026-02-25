import pygame


class Texture():
    def __init__(self, width:int, height:int) -> None:
        
        self.texture = pygame.Surface((width, height))

        self.width = width
        self.height = height

        self.sprites = {

        }


    def get_sprite(self, name:str) -> pygame.Surface:
        return self.sprites.get(name, pygame.Surface((32, 32)))


    def index_sprite(self, index) -> pygame.Surface:
        try:
            return list(self.sprites.values())[index]
        except Exception as e:
            print(f"ERROR: Texture: index_sprite: {e}")
            return pygame.Surface((self.width, self.height))


    def set_texture(self, img:pygame.Surface) -> None:
        #setting the sprite of this object
        self.sprite = img
        #updating w, h
        self.width = img.get_width()
        self.height = img.get_height()
    

    def add_spritesheet(self, src:str, sprite_w:int, sprite_h:int) -> None:

        #loading image with error handling
        try:
            spritesheet = pygame.image.load(src)
        except Exception as e:  
            print(f"ERROR: Texture: add_spritesheet: {e}")
            return

        total_sprites = spritesheet.get_width() // sprite_w

        #iterating through all found sprites
        for s in range(total_sprites):
            #getting sprite by finding pos on spritesheet surface
            new_sprite = pygame.Surface((sprite_w, sprite_h))
            new_sprite.blit(spritesheet, (0, 0), (sprite_w*s, 0, sprite_w, sprite_h))
            #adding new sprite to sprites dict
            self.sprites[f"{s}"] = new_sprite
                
        



        