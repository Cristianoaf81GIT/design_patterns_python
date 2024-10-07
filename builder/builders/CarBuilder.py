from datetime import datetime

from . import AbsctractBuilder
from products import Car

class CarBuilder(AbsctractBuilder):

    __car: Car

    def __init__(self, model: str) -> None:
        print("start building car....")
        self.__car = Car(seats=0, doors=0, manufacturing_date=datetime.now(), model=model)

    def reset(self) -> None:
        print("reseting car....")
        self.__car = Car(seats=0, doors=0, manufacturing_date=datetime.now(), model=self.__car.model)

    def set_seats(self, seats: int) -> None:
        print(f"adding {seats} to car...")
        self.__car.seats = seats

    def set_doors(self, doors: int) -> None:
        print(f"adding {doors} to car...")
        self.__car.doors = doors 

    def set_manufacturing_date(self, manufacturing_date: datetime) -> None:
        print(f"setting car manufacturing_date to : {manufacturing_date} ...")
        self.__car.manufacturing_date = manufacturing_date

    def build(self) -> Car:
        print("finishing build car!")
        return self.__car


