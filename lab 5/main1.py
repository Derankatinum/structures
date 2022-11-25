from Sort2 import merge_sort
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
        a=int(input(f'a {i} =  '))
        main_array.append(a)

    return main_array


main_array = auto_input()


print(f"Вхідний масив                      : {main_array}")
merge_sort(main_array)
print(f"Після сортування методом Merge Sort: {main_array}")





