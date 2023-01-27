def insertion_sort(string):
    s = len(string)

    for index in range(0, s):
        chave = string[index]  # pego o segundo elemento da lista

        new_position = index - 1  # tomamos a posição anterior para comparar

        while (
            new_position >= 0
            and string[new_position] > string[new_position + 1]
        ):
            string[new_position + 1] = string[new_position]
            new_position = new_position - 1

        string[new_position + 1] = chave

        return string


def is_anagram(first_string, second_string):
    first = list(first_string.lower())
    second = list(second_string.lower())

    insertion_sort(first)
    insertion_sort(second)

    if first == "" or second == "":
        return False

    if first == second:
        return ("".join(first), "".join(second), True)
    else:
        return ("".join(first), "".join(second), False)
