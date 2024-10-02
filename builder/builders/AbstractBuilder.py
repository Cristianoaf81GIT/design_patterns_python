from abc import ABCMeta, abstractmethod
from datetime import datetime

class AbsctractBuilder(metaclass=ABCMeta):

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod 
    def set_seats(self, seats: int) -> None:
        pass

    @abstractmethod
    def set_doors(self, doors: int) -> None:
        pass

    @abstractmethod
    def set_manufacturing_date(self, manufacturing_date: datetime) -> None:
        pass

    
