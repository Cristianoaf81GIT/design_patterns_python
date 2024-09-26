from abc import ABCMeta, abstractmethod


class CheckBox(metaclass=ABCMeta):
    @abstractmethod
    def paint(self) -> None:
        pass
