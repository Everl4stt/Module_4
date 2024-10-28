import time

def func_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'Время на выполнение функции {func.__name__} = {time.time() - start_time} секунд')
        return result
    return wrapper

@func_time
def merge_sort(mass):
    if len(mass) < 2:
        return mass[:]
    else:
        median = int(len(mass)/2)
        left = merge_sort(mass[:median])
        right = merge_sort(mass[median:])
        return merge(left, right)

@func_time
def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i +=1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

a = [12, 2, 34, 5, 1, 45, 16, 2, 7, 4]
print(f"Отсортированный массив: {merge_sort(a)}") #Сложность алгоритма O(n*log(n))