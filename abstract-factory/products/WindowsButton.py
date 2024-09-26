from products import Button


class WindowsButton(Button):
    def paint(self) -> None:
        print("Painting -> [WindowsButton]")
