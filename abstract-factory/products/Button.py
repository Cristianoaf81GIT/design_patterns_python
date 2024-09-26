from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def paint(self) -> None:
        pass
