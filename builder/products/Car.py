from datetime import datetime

class Car:
    __seats: int
    __doors: int
    __manufacturing_date: datetime
    __model: str

    def __init__(self, seats: int, doors: int, manufacturing_date: datetime, model: str) -> None:
        self.__seats = seats
        self.__doors = doors
        self.__manufacturing_date = manufacturing_date
        self.__model = model


    @property
    def seats(self) -> int:
        return self.__seats

    @seats.setter
    def set_seats(self, seats: int) -> None:
        self.__seats = seats
    
    @property
    def doors(self) -> int:
        return self.__doors

    @doors.setter
    def doors(self, doors: int) -> None:
        self.__doors = doors

    @property
    def manufacturing_date(self) -> datetime:
        return self.__manufacturing_date

    @manufacturing_date.setter
    def manufacturing_date(self, manufacturing_date: datetime) -> None:
        self.__manufacturing_date = manufacturing_date
    
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str) -> None:
        self.__model = model

    def __repr__(self) -> str:
        return f'Car(seats={self.__seats}, doors={self.__doors},manufacturing_date={self.__manufacturing_date}, model={self.__model})'

