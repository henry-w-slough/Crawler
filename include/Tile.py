import include.GameObject as GameObject


class Tile(GameObject.GameObject):
    def __init__(self, width, height, x, y, *groups) -> None:
        super().__init__(width, height, *groups)

        