from products import CheckBox


class WindowsCheckBox(CheckBox):
    def paint(self) -> None:
        print("Painting -> [WindowsCheckBox]")
