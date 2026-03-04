import pygame

import src.Engine.GameObject as GameObject

class Player(GameObject.GameObject):
    def __init__(self, width: int, height: int, *groups:pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.texture.add_sprites("assets/spritesheets/player.png", 4, "idle")
        self.image = self.texture.get_sprite("idle0")

        self.speed = 5

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.add_position(0, -self.speed)
            self.image = self.texture.get_sprite("idle1")
        if keys[pygame.K_s]:
            self.add_position(0, self.speed)
            self.image = self.texture.get_sprite("idle0")
        if keys[pygame.K_a]:
            self.add_position(-self.speed, 0)
            self.image = self.texture.get_sprite("idle2")
        if keys[pygame.K_d]:
            self.add_position(self.speed, 0)
            self.image = self.texture.get_sprite("idle3")

