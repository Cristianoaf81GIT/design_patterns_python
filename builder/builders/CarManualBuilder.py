from products import Manual
from . import AbsctractBuilder

from datetime import datetime

class CarManualBuilder(AbsctractBuilder):
    
    __manual: Manual
    __manual_data: str = ""

    def __init__(self, model: str, pages: int) -> None:
        print("start building car manual...")
        self.__manual = Manual(model=model, manufacturing_date=datetime.now(), pages=pages)
    
    def reset(self) -> None:        
        print("reseting car manual....")
        self.__manual = Manual(model=self.__manual.model or "", manufacturing_date=datetime.now(), pages=self.__manual.pages or 0)
    
    def set_seats(self, seats: int) -> None:
        print("setting number of seats into car manual....")
        self.__manual_data += f"car {self.__manual.model} with {seats} seats\n" 


    def set_doors(self, doors: int) -> None:
        print("setting number of doors info into car manual...")
        self.__manual_data += f"car {self.__manual.model} with {doors} doors\n"

    def set_manufacturing_date(self, manufacturing_date: datetime) -> None:
        print("setting car manual manufacturing_date...")
        self.__manual_data += f"car {self.__manual.model} with  manufacturing_date  to: {manufacturing_date}\n"
    
    def build(self) -> Manual:
        print("finishing build car manual!")
        return self.__manual

