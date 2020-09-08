class Car:

    def __init__(self, speed, colour, name, police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.police = police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановалась')

    def turn(self, direction):
        map = {
            'right': 'направо',
            'left': 'налево'
        }
        print(f'{self.name} повернула {map[direction]}')

    def showspeed(self):
        print("Скорость автомобиля:", self.speed)


class TownCar(Car):

    def __init__(self, speed, colour, name, police):
        super().__init__(speed, colour, name, police)

    def showspeed(self):
        super().showspeed()

        if self.speed > 60:
            print(f'Превышение скорости')


class SportCar(Car):

    def __init__(self, speed, colour, name, police):
        super().__init__(speed, colour, name, police)


class WorkCar(Car):

    def __init__(self, speed, colour, name, police):
        super().__init__(speed, colour, name, police)

    def showspeed(self):
        super().showspeed()

        if self.speed > 40:
            print(f'Превышение скорости')


class PoliceCar(Car):

    def __init__(self, speed, colour, name, police):
        super().__init__(speed, colour, name, police)
        
        
def main():
    """
    4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, ispolice
    (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
    повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод showspeed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод showspeed. При значении скорости свыше 60 (TownCar) и
    40 (WorkCar) должно выводиться сообщение о превышении скорости.
    """
    town_car = TownCar(70, 'синий', 'tayota', False)
    sport_car = SportCar(120, 'красный', 'porsche', False)
    work_car = WorkCar(30, 'белый', 'kia', False)
    police_car = PoliceCar(60, 'белый', 'lada', True)

    town_car.go()
    sport_car.go()
    work_car.go()
    police_car.go()

    town_car.turn('left')
    town_car.showspeed()


if __name__ == '__main__':
    main()
