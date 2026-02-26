import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Sprite) -> None:
        super().__init__(*groups)

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()

    def set_position(x:int, y:int) -> None:
        self.rect.x = x
        self.rect.y = y

    