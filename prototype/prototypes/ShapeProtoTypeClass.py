from typing import Self
from abc import ABCMeta, abstractmethod


class ShapePrototype(metaclass=ABCMeta):
    x: int
    y: int
    color: str

    def __init__(self, source: Self) -> None:
        self.x = source.x
        self.y = source.y
        self.color = source.color

    @abstractmethod
    def clone(self) -> Self:
        pass
