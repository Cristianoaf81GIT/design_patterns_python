from abc import ABCMeta, abstractmethod

from products import Button
from products.CheckBox import CheckBox


class GuiFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass
