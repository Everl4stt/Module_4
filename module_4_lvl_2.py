def insertion_sort(a):
        for i in range(1, len(a)):
            x = a[i]
            while i - 1 >= 0 and a[i - 1] > x:
                a[i] = a[i - 1]
                i -= 1
            a[i] = x
        return a
a = [12, 3, 4, 5, 67, 2, 78, 9, 34, 99, 1, 1]
print("Изначальный массив: ", a)
print("Отсортированный массив: ", insertion_sort(a))
