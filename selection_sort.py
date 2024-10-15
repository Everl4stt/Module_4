def selection_sort(a):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(a)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(a)):
            if a[j] < a[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        a[i], a[lowest_value_index] = a[lowest_value_index], a[i]

# Проверяем, что оно работает
a = [12, 8, 3, 20, 11, 23, 4, 56, 7]
selection_sort(a) #Сложность алгоритма O(n^2)
print(a)