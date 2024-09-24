from typing import Any
from products import Button


class WindowButton(Button):

    def render(self) -> None:
        print("[WindowsButton is] -> rendering")

    def on_click(self, event: Any) -> None:
        print(f"[WindowsButton is]: handling event -> {event}")

