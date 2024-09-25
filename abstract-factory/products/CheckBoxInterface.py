from abc import ABCMeta, abstractmethod

class CheckBoxInterface(metaclass=ABCMeta):

    @abstractmethod
    def paint(self) -> None:
        pass
