def is_anagram(first_string, second_string):
    first = list(first_string.lower())
    second = list(second_string.lower())

    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    merge_sort(first)
    merge_sort(second)

    palavra1 = "".join(first)
    palavra2 = "".join(second)

    if palavra1 == palavra2:
        return (palavra1, palavra2, True)
    else:
        return (palavra1, palavra2, False)


def merge_sort(string, start=0, end=None):
    if end is None:
        end = len(string)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(string, start, mid)
        merge_sort(string, mid, end)
        merge(string, start, mid, end)


def merge(string, start, mid, end):
    left = string[start:mid]
    right = string[mid:end]
    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            string[general_index] = right[right_index]
            right_index = right_index + 1
