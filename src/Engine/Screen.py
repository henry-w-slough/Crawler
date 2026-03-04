import pygame
import src.Engine.Texture as Texture
import src.Engine.Camera as Camera


class Screen():
    def __init__(self, width:int, height:int) -> None:
        """Handles any screen-related logic needed for a game. Updates all objects added to it's layers dict and updates the display."""
        
        self.screen = pygame.display.set_mode((width, height))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.width = width
        self.height = height

        self.layers = {
            "tiles": pygame.sprite.Group(),
            "player": pygame.sprite.Group(),
            "visible": pygame.sprite.Group()
        }
    
    def start(self) -> None:
        self.camera = Camera.Camera(list(self.layers["player"])[0])

    def update(self) -> None:


        self.layers["visible"].add(self.camera.get_visible(self.layers["tiles"]))
        self.layers["visible"].add(self.camera.get_visible(self.layers["player"]))

        #filling screen with black
        self.screen.fill((0, 0, 0))

        for id, layer in self.layers.items():
            #this iterates through every item and updates
            #only draws the visible items, as said by a Camera object
            layer.update()
            if id == "visible":
                layer.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(self.fps)




