def binary_search(a, targ):
    middle = int((len(a) / 2))
    print(a, a[middle])
    if targ == a[middle] :
        print("Искомый элемент найден")
        return print(a[middle])
    elif len(a) == 1 and a[middle] != targ:
        print("Искомого элемента нет в массиве")
        return 0
    else:
        left = []
        right = []
        if targ > a[middle]:
            right = binary_search(a[middle:], targ)
        else :
            left = binary_search(a[:middle], targ)

a = [4, 6, 8, 10, 13, 16, 23, 45, 56, 65, 78, 87, 88, 98, 100]
targ = 4
binary_search(a, targ)