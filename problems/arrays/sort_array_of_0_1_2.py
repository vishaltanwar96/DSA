def sort012(array: list[int]):
    c0, c1, c2 = 0, 0, 0

    for element in array:
        if element == 0:
            c0 += 1
        elif element == 1:
            c1 += 1
        else:
            c2 += 1
    i = 0
    while c0 > 0:
        array[i] = 0
        i += 1
        c0 -= 1

    while c1 > 0:
        array[i] = 1
        i += 1
        c1 -= 1

    while c2 > 0:
        array[i] = 2
        i += 1
        c2 -= 1

    return array
