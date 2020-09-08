class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        pass


class Pen(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "ручка"


class Pencil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "карандаш"


class Handle(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "маркер"
    
    
def main():
    """
    6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
    draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
    Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
    что выведет описанный метод для каждого экземпляра.
    """
    pen = Pen('ручка')
    pencil = Pencil('карандаш')
    handle = Handle('маркер')

    print(pen.draw())
    print(pencil.draw())
    print(handle.draw())


if __name__ == '__main__':
    main()
