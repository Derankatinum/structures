def merge_sort(main_array):
    if len(main_array) > 1:
        mid = len(main_array) // 2  # Пошук половини масиву
        left = main_array[:mid]  # Запис поділу лівої частини
        right = main_array[mid:]  # Запис поділу правої частини

        merge_sort(left)  # Рекурсія і виклик функції з вхідною лівою частиною
        merge_sort(right)  # Рекурсія і виклик функції з вхідною правою частиною

        i, j, k = 0, 0, 0  # Змінні для циклів

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                main_array[k] = left[i]
                i += 1
            else:
                main_array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):  # Перевірка, чи залишився якийсь елемент
            main_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            main_array[k] = right[j]
            j += 1
            k += 1
