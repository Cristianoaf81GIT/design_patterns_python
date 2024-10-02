from datetime import datetime


class Manual:

    __model: str
    __manufacturing_date: datetime
    __pages: int


    def __init__(self, model: str, manufacturing_date: datetime, pages: int) -> None:
        self.__model = model
        self.__manufacturing_date = manufacturing_date
        self.__pages = pages


    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str) -> None:
        self.__model = model 

    @property
    def manufacturing_date(self) -> datetime:
        return self.__manufacturing_date

    @manufacturing_date.setter
    def manufacturing_date(self, manufacturing_date: datetime) -> None:
        self.__manufacturing_date = manufacturing_date

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int) -> None:
        self.__pages = pages


    def __repr__(self) -> str:
        return f'Manual(model={self.__model}, manufacturing_date={self.__manufacturing_date}, pages={self.__pages})'
    
