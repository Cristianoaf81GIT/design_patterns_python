from typing import TypedDict
import random


class GuiConfig(TypedDict):
    OS: str


def read_application_config_file() -> GuiConfig:
    __oses = ["windows", "linux"]
    __selection = round(random.uniform(0, 1))

    return {"OS": __oses[__selection]}
