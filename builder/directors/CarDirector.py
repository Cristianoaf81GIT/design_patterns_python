from datetime import datetime
from builders import AbsctractBuilder

class CarDirector:

    def construct_sport_car(self, builder: AbsctractBuilder) -> None:
        builder.reset()
        builder.set_seats(2)
        builder.set_doors(2)
        builder.set_manufacturing_date(datetime.now())

    def construct_suv_car(self, builder: AbsctractBuilder) -> None:
        builder.reset()
        builder.set_seats(6)
        builder.set_doors(4)
        builder.set_manufacturing_date(datetime.now())
