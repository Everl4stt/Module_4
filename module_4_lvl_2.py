def insertion_sort(a):
    if len(a) == 1:
        return a
    else:
        for i in range(len(a)):
            for j in range(i):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
        return a
a = [12, 3, 4, 5, 67, 2, 78, 9, 34]
print("Изначальный массив: ", a)
print("Отсортированный массив: ", insertion_sort(a))
