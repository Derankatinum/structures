from random import randint

"""
PART 1
"""


def quick_sort(main_array):
    if len(main_array) <= 1:  # Умова виходу з рекурсії
        return main_array

    supporting_element = main_array[len(main_array) - 1]  # Опорний елемент (Останній в масиві)

    # supporting_element = randint(0, int(len(main_array) - 1))  # Опорний елемент (Рандомно)

    left_part = list(filter(lambda x: x < supporting_element, main_array))  # Лiва частина

    # Центральна частина
    # На випадок якщо є багато елементів які == опорному
    center_part = []
    for i in main_array:
        if i == supporting_element:
            center_part.append(i)

    right_part = list(filter(lambda x: x > supporting_element, main_array))  # Права частина

    return quick_sort(left_part) + center_part + quick_sort(right_part)


"""
PART 2
"""


def select_statistic(main_array, i):  # Функція пошуку порядкової статистики
    buffer_array = quick_sort(main_array)
    task_2_3(buffer_array)  # Виклик завдання Частина_2_2
    return buffer_array[int(i) - 1]


def task_2_3(main_array) -> None:  # Завдання Частина_2_2
    print(f"Максимальне значення: {max(main_array)}")
    print(f"Мінімальне значення: {min(main_array)}")

    buffer_median = []

    if len(main_array) % 2 == 1:
        buffer_median.append(main_array[len(main_array) // 2])
        print(f"Медіана: {buffer_median}")
    else:
        buffer_median.append(main_array[len(main_array) // 2])
        buffer_median.append(main_array[(len(main_array) // 2) - 1])
        print(f"Медіана: {buffer_median}")


