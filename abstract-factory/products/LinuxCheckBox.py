from products import CheckBoxInterface

class LinuxCheckBox(CheckBoxInterface): #pyright: ignore

    def paint(self) -> None:
        print("Painting [LinuxCheckBox]")
