from typing import List, Any


class House:
    houses_history = []
    __instance = None
    number_one = 0

    def __new__(cls, *args, **kwargs):
        # print('Я в ньюшке')
        cls.houses_history.append(args[0])
        cls.number_one += 1
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, number_of_floors):
        # print('Я в ините, ничо нинаю')
        # self.args = args
        self.name = name
        self.number_of_floors = number_of_floors
        self.number_one = 0

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        isinstance(other, int)
        if self.number_of_floors == other:
            return True
        else:
            return False

    def __lt__(self, other):
        isinstance(other, int)
        if self.number_of_floors < other:
            return True
        else:
            return False

    def __le__(self, other):
        isinstance(other, int)
        if self.number_of_floors <= other:
            return True
        else:
            return False

    def __gt__(self, other):
        isinstance(other, int)
        if self.number_of_floors > other:
            return True
        else:
            return False

    def __ge__(self, other):
        isinstance(other, int)
        if self.number_of_floors >= other:
            return True
        else:
            return False

    def __ne__(self, other):
        isinstance(other, int)
        if self.number_of_floors != other:
            return True
        else:
            return False

    def __add__(self, value):
        isinstance(value, int)
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        isinstance(value, int)
        self.number_of_floors = value + self.number_of_floors
        return self

    def __iadd__(self, value):
        isinstance(value, int)
        self.number_of_floors += value
        return self

    def __delitem__(self, index: object) -> object:
        class_name = House.houses_history[index]
        print('{} уничтожен, но останется в истории'.format(class_name))
        # self.name = House.houses_history[0]
        # print('{} снесён, но останется в истории'.format(self.name))


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 10)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

House.__delitem__(House.houses_history, 0)

House.__delitem__(House.houses_history, 2)
print(House.houses_history)
# del House.houses_history[2]
