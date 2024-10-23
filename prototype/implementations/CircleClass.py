from typing import Self
import copy

from prototypes import ShapePrototype


class Circle(ShapePrototype):
    radius: int

    def __init__(self, source: Self) -> None:
        super().__init__(source)
        self.radius = source.radius

    def clone(self) -> Self:
        return copy.deepcopy(self)
