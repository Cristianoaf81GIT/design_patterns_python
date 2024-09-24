from products import Button
from products import HtmlButton
from . import Dialog

class WebDialog(Dialog):

    def create_button(self) -> Button:
        return HtmlButton() 

