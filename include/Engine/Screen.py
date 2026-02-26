import pygame
import include.Engine.Texture as Texture


class Screen():
    def __init__(self, width:int, height:int) -> None:
        
        self.screen = pygame.display.set_mode((width, height))

        self.texture = Texture.Texture(width, height)
        self.texture.add_sprites("assets/spritesheets/background.png", 1, "background")
        
        self.background = self.texture.get_sprite("background0")

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.width = width
        self.height = height

        self.layers = {
            "tiles": pygame.sprite.Group()
        }

    def update(self) -> None:

        #displaying the background (noteably before all layers)
        self.screen.blit(self.background, (0, 0))

        for layer in self.layers.values():
            layer.update()
            layer.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(self.fps)




