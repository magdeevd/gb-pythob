from time import sleep


class TrafficLight:

    def __init__(self):
        self.__colour = 'red'

    def running(self):
        print(self.__colour)
        sleep(7)
        self.__colour = 'yellow'
        print(self.__colour)
        sleep(2)
        self.__colour = 'green'
        print(self.__colour)
        sleep(5)
        self.__colour = 'red'


def main():
    """
    1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
    зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
    (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
    (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
    """
    traffic_light = TrafficLight()
    traffic_light.running()


if __name__ == '__main__':
    main()
