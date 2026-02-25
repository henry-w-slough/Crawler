import pygame
import include.Texture as Texture


class Screen():
    def __init__(self, width:int, height:int) -> None:
        
        self.screen = pygame.display.set_mode((width, height))

        self.texture = Texture.Texture(width, height)
        self.texture.add_spritesheet("assets/background.png", width, height)
        self.texture.set_texture(self.texture.get_sprite("0"))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.width = width
        self.height = height

        self.layers = {

        }


    def update(self):

        self.screen.blit(self.texture.texture, (0, 0))


        pygame.display.flip()
        self.clock.tick(self.fps)




