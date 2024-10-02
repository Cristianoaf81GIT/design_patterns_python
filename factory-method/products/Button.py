from abc import ABCMeta, abstractmethod
from typing import Any 

class Button(metaclass=ABCMeta):

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def on_click(self, event: Any) -> None:
        pass

