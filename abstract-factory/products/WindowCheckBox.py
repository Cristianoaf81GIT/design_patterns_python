from products import CheckBoxInterface

class WindowsCheckBox(CheckBoxInterface): #pyright: ignore 

    def paint(self) -> None:
        print("Painting -> [WindowsCheckBox]")

