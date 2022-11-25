from Sort import counting_sort, counting_sort_task_3, radix_sort, radix_sort_task_3, radix_sort_task_3_2
from random import randint


print(10 // 3)

"""
Автоматичне введення в масив
"""



main_array = []
sec_array = []
number_of_elements = (input(f"Вкажіть кількість елементів в масиві: "))
frame_min_number = 0
frame_max_number = int(input(f"Вкажіть максимальне число яке може входити в масив: "))
for i in range(int(number_of_elements)):
     a = int(input(f'a {i} =  '))
     if a>=0:
         sec_array.append(a)
         if a >= 0 and a <= 9:
             main_array.append(a)




"""
PART 1
"""

print(f"Вхідний масив                                : {main_array}")

print(f"Після сортування методом Підрахунку          : {counting_sort(main_array)}")

print(f"Після сортування методом Підрахунку обернений: {counting_sort_task_3(main_array)}")


"""
PART 2
"""
print("---------------------------------------------")


print(f"Вхідний масив                              : {sec_array}")

print(f"Після сортування за розрядами              : {radix_sort(sec_array)}")

print(f"Після сортування за розрядами обернений 3.1: {radix_sort_task_3(sec_array)}")

print(f"Після сортування за розрядами обернений 3.2: {radix_sort_task_3_2(sec_array)}")

print("---------------------------------------------")

