from factories import GuiFactory
from products import Button


class ApplicationGui:
    __factory: GuiFactory
    __button: Button

    def __init__(self, factory: GuiFactory) -> None:
        self.__factory = factory

    def create_ui(self) -> None:
        self.__button = self.__factory.create_button()

    def paint(self) -> None:
        self.__button.paint()
