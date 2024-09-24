from typing import Any
from products import Button


class HtmlButton(Button):

    def render(self) -> None:
        print("[HtmlButton is] -> rendering")

    def on_click(self, event: Any) -> None:
        print(f"[HtmlButton is]: handling event -> {event}")
