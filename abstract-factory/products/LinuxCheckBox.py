from products import CheckBox


class LinuxCheckBox(CheckBox):  # pyright: ignore
    def paint(self) -> None:
        print("Painting [LinuxCheckBox]")
