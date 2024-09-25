from abc import ABCMeta, abstractmethod 

class ButtonInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def paint(self) -> None:
        pass
