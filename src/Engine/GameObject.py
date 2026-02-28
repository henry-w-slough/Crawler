import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        super().__init__(*groups)

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()

    def set_position(self, x:int, y:int) -> None:
        self.rect.x = x
        self.rect.y = y

    