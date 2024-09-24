from abc import abstractmethod

from products import Button

class Dialog:

    @abstractmethod 
    def create_button(self) -> Button:
        pass

    def render(self) -> None:
        ok_button: Button = self.create_button()
        ok_button.on_click("CLOSE_DIALOG")
        ok_button.render()
