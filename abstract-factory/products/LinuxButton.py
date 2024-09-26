from products import Button


class LinuxButton(Button):
    def paint(self) -> None:
        print("Painting -> [LinuxButton]")
