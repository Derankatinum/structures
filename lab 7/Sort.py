"""
PART 1
"""


def counting_sort(main_array):  # Функція CountingSort(…) для реалізації сортування методом підрахунку.
    buffer_array = []
    array_exp = []
    for j in range(max(main_array) + 1):
        buffer_array.append(0)

    # print(buffer_array)

    for i in range(len(main_array)):
        buffer_array[main_array[i - 1]] += 1

    # print(buffer_array)

    for i in range(len(buffer_array)):
        if buffer_array[i] > 0 and buffer_array[i]<10:
            for j in range(buffer_array[i]):
                array_exp.append(i)
        else:
            continue

    return array_exp


def counting_sort_task_3(main_array):  # Функція CountingSort(…) для реалізації сортування методом підрахунку.
    # Зі зміненим порядком проходження останнього циклу (зі спадання на зростання)
    buffer_array = []
    array_exp = []
    for j in range(max(main_array) + 1):
        buffer_array.append(0)

    # print(buffer_array)

    for i in range(len(main_array)):
        buffer_array[main_array[i - 1]] += 1

    # print(buffer_array)

    i = len(buffer_array) - 1
    while i >= 0:

        if buffer_array[i] != 0:

            for j in range(buffer_array[i]):
                array_exp.append(i)
                i -= 1

        else:
            i -= 1
            continue

    return array_exp


"""
PART 2
"""


def counting_sort_for_radix(main_array, place_value):

    count_array = [0] * 10
    main_array_size = len(main_array)

    for i in range(main_array_size):
        place_element = (main_array[i] // place_value) % 10
        count_array[place_element] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    array_exp = [0] * main_array_size  # Вихідний масив

    i = main_array_size - 1
    while i >= 0:
        current_element = main_array[i]
        place_element = (main_array[i] // place_value) % 10
        count_array[place_element] -= 1
        new_position = count_array[place_element]
        array_exp[new_position] = current_element
        i -= 1

    return array_exp


def radix_sort(main_array):

    max_element = max(main_array)  # Знаходить максимальний елемент у вхідному масиві

    number_of_digits_in_max = len(str(max_element))  # Кількість цифр в максимальному елементі

    place_value = 1

    output_array = main_array
    while number_of_digits_in_max > 0:
        output_array = counting_sort_for_radix(output_array, place_value)
        place_value *= 10
        number_of_digits_in_max -= 1

    return output_array


def counting_sort_for_radix_task_3(main_array, place_value):

    count_array = [0] * 10
    main_array_size = len(main_array)

    for i in range(main_array_size):
        place_element = (main_array[i] // place_value) % 10
        count_array[place_element] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    array_exp = [0] * main_array_size  # Вихідний масив

    i = 0
    while i <= main_array_size - 1:
        current_element = main_array[i]
        place_element = (main_array[i] // place_value) % 10
        count_array[place_element] -= 1
        new_position = count_array[place_element]
        array_exp[new_position] = current_element
        i += 1

    return array_exp


def radix_sort_task_3(main_array):

    max_element = max(main_array)  # Знаходить максимальний елемент у вхідному масиві

    number_of_digits_in_max = len(str(max_element))  # Кількість цифр в максимальному елементі

    place_value = 1

    output_array = main_array
    while number_of_digits_in_max > 0:
        output_array = counting_sort_for_radix_task_3(output_array, place_value)
        place_value *= 10
        number_of_digits_in_max -= 1

    return output_array


def counting_sort_for_radix_task_3_2(main_array, place_value):

    count_array = [0] * 10
    main_array_size = len(main_array)

    for i in range(main_array_size):
        place_element = (main_array[i] // place_value) % 10
        count_array[place_element] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    array_exp = [0] * main_array_size  # Вихідний масив

    i = main_array_size - 1
    while i >= 0:
        current_element = main_array[i]
        place_element = (main_array[i] // place_value) % 10
        count_array[place_element] -= 1
        new_position = count_array[place_element]
        array_exp[new_position] = current_element
        i -= 1

    return array_exp


def radix_sort_task_3_2(main_array):

    max_element = max(main_array)  # Знаходить максимальний елемент у вхідному масиві

    number_of_digits_in_max = len(str(max_element))  # Кількість цифр в максимальному елементі

    place_value = 1

    output_array = main_array
    i = 0
    while i < number_of_digits_in_max:
        output_array = counting_sort_for_radix_task_3_2(output_array, place_value)
        place_value *= 10
        i += 1

    return output_array

