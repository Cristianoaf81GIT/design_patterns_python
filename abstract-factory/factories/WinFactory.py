from factories import GuiFactory
from products import Button
from products import CheckBox
from products import WindowsButton
from products import WindowsCheckBox


class WinFactory(GuiFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()
