import pygame
import src.Engine.Texture as Texture

class GameObject(pygame.sprite.Sprite):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        """Represents any object on the screen. Has a rectangle, position and texture."""
        super().__init__(*groups)

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()

        self.texture = Texture.Texture(width, height)

    def set_position(self, x:int, y:int) -> None:
        """Sets the x and y values of the object to the given."""
        self.rect.x = x
        self.rect.y = y

    