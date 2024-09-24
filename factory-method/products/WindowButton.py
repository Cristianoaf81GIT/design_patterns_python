from typing import Any
from products import Button


class WindowButton(Button):

    def render(self) -> None:
        print("[WindowButton is] -> rendering")

    def on_click(self, event: Any) -> None:
        print(f"[WindowButton is]: handling event -> {event}")

