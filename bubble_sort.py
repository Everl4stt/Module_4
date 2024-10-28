import time

def func_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'Время на выполнение функции {func.__name__} = {time.time() - start_time} секунд')
        return result
    return wrapper

@func_time
def bubble_sort(a) :
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
a = [12, 2, 34, 5, 6, 9, 19, 4, 2, 23, 45, 56, 2, 23, 56, 67, 8, 10]
print("Отсортированный массив: ", bubble_sort(a)) #Сложность алгоритма O(n^2)