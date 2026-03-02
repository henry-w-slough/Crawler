from pygame.sprite import Group

import src.Engine.GameObject as GameObject

class Player(GameObject.GameObject):
    def __init__(self, width: int, height: int, *groups: Group) -> None:
        super().__init__(width, height, *groups)

        self.texture.add_sprites("assets/spritesheets/player.png", 4, "idle")
        self.image = self.texture.get_sprite("idle0")