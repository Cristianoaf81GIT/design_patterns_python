from products import Button
from products import WindowButton
from . import Dialog


class WindowsDialog(Dialog):

    def create_button(self) -> Button:
        return WindowButton()


