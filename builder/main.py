from directors import CarDirector, CarManualDirector
from builders import CarBuilder, CarManualBuilder

def main():
    car_director = CarDirector()
    car_manual_director = CarManualDirector()

    car_builder = CarBuilder("sport")
    car_manual_builder = CarManualBuilder("sport", 200)

    car_director.construct_sport_car(car_builder)
    car_manual_director.construct_sport_car_manual(car_manual_builder)
    
    car = car_builder.build()
    car_manual = car_manual_builder.build()
    
    print(f'{car.__repr__()}')
    print(f'{car_manual.__repr__()}')


if __name__ == "__main__":
    main()
