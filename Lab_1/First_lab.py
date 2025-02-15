# from random import uniform
# import datetime
#
#
# def insertion_sort(our_mass, sorted_mass, count_entering_the_array = 0, count_exchange = 0):
#     start_time = datetime.datetime.now()
#
#
#     for elem_id in range(1, len(our_mass)):
#         count_entering_the_array += 1
#         for next_elem_id in range(elem_id, 0, -1):
#             if our_mass[next_elem_id - 1] > our_mass[next_elem_id]:
#                 count_exchange += 1
#                 our_mass[next_elem_id], our_mass[next_elem_id - 1] = our_mass[next_elem_id - 1], our_mass[next_elem_id]
#         if our_mass == sorted_mass:
#             finish_time = datetime.datetime.now()
#             return [(finish_time - start_time).microseconds, count_entering_the_array, count_exchange]
#
#
#
# dimensions = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]
# result = []
#
# for dimension in dimensions:
#     for approach in range(20):
#         mass = [uniform(-1, 1) for _ in range(dimension)]
#         tmp = sorted(mass.copy())
#         result.append({dimension:{approach + 1:insertion_sort(mass, tmp)}})
#
# for elem in result:
#     for data in elem:
#         with open("results.txt", "a", encoding='utf-8') as file:
#             file.write(f"{data}: {elem.get(data)}\n")


import re
import numpy as np
import matplotlib.pyplot as plt

# Чтение данных из файла
def read_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            # Используем регулярные выражения для извлечения данных
            match = re.match(r"(\d+)\s+Time taken: ([\d.]+)\s+seconds,\s+Entries:\s+(\d+),\s+Exchanges:\s+(\d+)"
                             , line)
            if match:
                size = int(match.group(1))
                time_taken = float(match.group(2))
                entries = int(match.group(3))
                exchanges = int(match.group(4))
                data.append((size, time_taken, entries, exchanges))
    return data

data = read_data(r"C:\Users\nikit\OneDrive\Рабочий стол\Lab\datas.txt") #<------------ берем из txt файла после прогонки
                                                                                # серии сортировок при помощи языка C
sizes = [item[0] for item in data]
times = [item[1] for item in data]
entries = [item[2] for item in data]
exchanges = [item[3] for item in data]

# График зависимости времени от размера массива
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, label='Время выполнения', color='blue', marker='o')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (сек.)')
plt.title('Зависимость времени от размера массива')
plt.grid(True)
plt.legend()
plt.show()

# График наихудшего времени и O(N^2)
plt.figure(figsize=(10, 6))

# Наихудшее время
plt.plot(sizes, times, label='Наихудшее время', color='blue', marker='o')

# O(N^2) (с константой с)
O_N2 = [c * size**2 for size, c in zip(sizes, [0.000001]*len(sizes))]  # Подбираем c
plt.plot(sizes, O_N2, label='O(N^2)', color='red', linestyle='--')

plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (сек.)')
plt.title('Наихудшее время и O(N^2)')
plt.grid(True)
plt.legend()
plt.show()

# Для среднего времени можно подсчитать среднее по каждому размеру
# Например, можно подсчитать по каждой группе данных
unique_sizes = sorted(set(sizes))
avg_times = []
min_times = []
max_times = []

for size in unique_sizes:
    filtered_times = [t for i, t in enumerate(times) if sizes[i] == size]
    avg_times.append(np.mean(filtered_times))
    min_times.append(np.min(filtered_times))
    max_times.append(np.max(filtered_times))

plt.figure(figsize=(10, 6))
plt.plot(unique_sizes, avg_times, label='Среднее время', color='green')
plt.plot(unique_sizes, min_times, label='Наилучшее время', color='orange')
plt.plot(unique_sizes, max_times, label='Наихудшее время', color='red')

plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (сек.)')
plt.title('Среднее, наилучшее и наихудшее время выполнения')
plt.grid(True)
plt.legend()
plt.show()

# График количества обменов
plt.figure(figsize=(10, 6))
plt.plot(sizes, exchanges, label='Количество обменов', color='purple', marker='x')
plt.xlabel('Размер массива')
plt.ylabel('Количество обменов')
plt.title('Зависимость количества обменов от размера массива')
plt.grid(True)
plt.legend()
plt.show()

# График количества сравнений (обходов массива)
plt.figure(figsize=(10, 6))
plt.plot(sizes, entries, label='Количество сравнений', color='brown', marker='s')
plt.xlabel('Размер массива')
plt.ylabel('Количество сравнений')
plt.title('Зависимость количества сравнений от размера массива')
plt.grid(True)
plt.legend()
plt.show()
