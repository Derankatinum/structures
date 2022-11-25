from Sort3 import quick_sort, select_statistic
from random import randint


"""
Автоматичне введення в масив
"""


def auto_input():
    main_array = []
    number_of_elements = (input(f"Вкажіть кількість елементів в масиві: "))
    frame_min_number = 0
    frame_max_number = int(input(f"Вкажіть максимальне число яке може входити в масив: "))
    for i in range(int(number_of_elements)):
        a = int(input(f'a {i} =  '))
        main_array.append(a)

    return main_array


main_array = auto_input()

"""
PART 1
"""

print(f"Вхідний масив                                : {main_array}")

print(f"Після сортування методом Quick Sort          : {quick_sort(main_array)}")


"""
PART 2
"""


print("---------------------------------------------")

print("Зауваження!! Номер порядкової статистики не має перевищувати кількість елементів в масиві!!")
i_index = input(f"Введіть номер порядкової статистики яку хочете знайти: ")
if int(i_index) > len(main_array) or int(i_index) < 0:
    print("Введено дані котрі не підлягають умові ):")
    print("Скоріше всього номер порядкової статистики перевищує кількість елементів в масиві!!")
else:
    print(f"Вхідний масив: {main_array}")

    print(f"Результат пошуку порядкової статистики: {select_statistic(main_array, i_index)}")

    print("---------------------------------------------")

