def partition_integers(array: list[int]):

    i, j = 0, len(array) - 1
    while i < j:

        if array[i] < 0 < array[j]:
            i += 1
            j -= 1
        elif array[i] > 0 and array[j] > 0:
            j += 1
        elif array[i] < 0 and array[j] < 0:
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
    return array
