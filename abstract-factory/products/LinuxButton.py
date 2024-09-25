from products import ButtonInterface

class LinuxButton(ButtonInterface):

    def paint(self) -> None:
        print("Painting -> [LinuxButton]")

