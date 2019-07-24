
import sys, random



class SumMemory:

    def __init__(self):
        """
        _sum_memory - общее количество занятой памяти
        _types - словарь вида {'type': [count, size]}
        """
        self._sum_memory = 0
        self._types = {}

    def extend(self, *args):
        for obj in args:
            self._add(obj)

    def _add(self, obj):
        spam = sys.getsizeof(obj)
        eggs = str(type(obj))
        self._sum_memory += spam
        if eggs in self._types:
            self._types[eggs][0] += 1
            self._types[eggs][1] += spam
        else:
            self._types[eggs] = [1, 1]
            self._types[eggs][1] = spam

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    self._add(key)
                    self._add(value)
            elif not isinstance(obj, str):
                for item in obj:
                    self._add(item)

    def print_sum(self):
        print(f'Переменные заняли в сумме {self._sum_memory} байт')
        for key, value in self._types.items():
            print(f'Объекты класса {key} в количестве {value[0]} заняли {value[1]} байт')



def sum_memory(objects):
    sum_mem = 0
    unique_id = set()
    for key, value in objects.items():
        if key.startswith('__'):
            # убираем "магию"
            continue
        elif hasattr(value, '__call__'):
            # убираем функции
            continue
        elif hasattr(value, '__loader__'):
            # убираем модули
            continue
        elif id(value) in unique_id:
            # убираем объекты (переменные), которые уже попали в сумму
            continue
        else:
            """
            Тут должен быть крутой цикл из прошлого примера
            """
            unique_id.add(id(value))
            sum_mem += sys.getsizeof(value)
            print(f'переменная {key} класса {type(value)} хранит {value} '
                  f'и занимает {sys.getsizeof(value)} байт')

    return sum_mem



SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)


for i in range(2, len(array)):
    if array[i] < array[min_first]:
        spam = min_first
        min_first = i
        if array[spam] < array[min_second]:
            min_second = spam

    elif array[i] < array[min_second]:
        min_second = i

print(f'Число {array[min_first]} в ячейке {min_first}')
print(f'Число {array[min_second]} в ячейке {min_second}')


print(sum_memory(locals()))