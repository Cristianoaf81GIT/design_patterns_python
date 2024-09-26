from factories import GuiFactory
from products import CheckBox, Button, LinuxCheckBox, LinuxButton


class LinuxFactory(GuiFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> CheckBox:
        return LinuxCheckBox()
