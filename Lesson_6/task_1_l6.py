# Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков. Проанализировать
# результат и определить программы с наиболее эффективным использованием
# памяти. Примечание: По аналогии с эмпирической оценкой алгоритмов
# идеальным решением будет: ● выбрать хорошую задачу, которую имеет смысл
# оценивать по памяти; ● написать 3 варианта кода (один у вас уже есть); ●
# проанализировать 3 варианта и выбрать оптимальный; ● результаты анализа
# (количество занятой памяти в вашей среде разработки) вставить в виде
# комментариев в файл с кодом. Не забудьте указать версию и разрядность
# вашей ОС и интерпретатора Python; ● написать общий вывод: какой из трёх
# вариантов лучше и почему. Надеемся, что вы не испортили программы,
# добавив в них множество sys.getsizeof после каждой переменной, а проявили
# творчество, фантазию и создали универсальный код для замера памяти.



import random, sys


#Определить, какое число в массиве встречается чаще всего.


SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100
sum_ = 0
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

n = arr[0]  # число
sum_ += sys.getsizeof(n)
n_frq = 0  # частота
sum_ += sys.getsizeof(n_frq)

for i in range(len(arr)):
    frq = 1
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            frq += 1
    if frq > n_frq:
        n_frq = frq
        n = arr[i]

if n_frq > 1:
    print(n_frq, 'times -', n)
else:
    print("no duplicates")


sum_ += sys.getsizeof(n)
sum_ += sys.getsizeof(n_frq)

print(sum_)

# 54 байт выделено памяти


# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
summ_ = 0
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)
summ_ += sys.getsizeof(min_first)
summ_ += sys.getsizeof(min_second)

for i in range(2, len(array)):
    if array[i] < array[min_first]:
        spam = min_first
        summ_ += sys.getsizeof(spam)
        min_first = i
        summ_ += sys.getsizeof(min_first)
        if array[spam] < array[min_second]:
            min_second = spam
            summ_ += sys.getsizeof(min_second)

    elif array[i] < array[min_second]:
        min_second = i
        summ_ += sys.getsizeof(min_second)

print(f'Число {array[min_first]} в ячейке {min_first}')
print(f'Число {array[min_second]} в ячейке {min_second}')
print(summ_)

# 106 байт выделено памяти




