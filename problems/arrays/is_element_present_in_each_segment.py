def is_present_in_each_segment(array: list[int], element: int, segment_size: int) -> bool:

    i = 0
    j = segment_size - 1
    is_present = False
    length_of_array = len(array)
    end_index = length_of_array - 1

    while i < length_of_array:

        if array[i] == element:
            is_present = True
            i = j + 1
            potential_j = j + segment_size
            j = potential_j if potential_j < end_index else end_index
        else:
            if i < j:
                i += 1
            else:
                is_present = False
                break
    return is_present
