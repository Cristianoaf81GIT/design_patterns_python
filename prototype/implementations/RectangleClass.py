from typing import Self
import copy

from prototypes import ShapePrototype


class Rectangle(ShapePrototype):
    width: int
    height: int

    def __init__(self, source: Self) -> None:
        super().__init__(source)
        self.width = source.width
        self.height = source.height

    def clone(self) -> Self:
        return copy.deepcopy(self)
