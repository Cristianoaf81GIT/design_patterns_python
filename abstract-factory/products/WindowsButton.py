from products import ButtonInterface

class WindowsButton(ButtonInterface):

    def paint(self) -> None:
        print("Painting -> [WindowsButton]")
