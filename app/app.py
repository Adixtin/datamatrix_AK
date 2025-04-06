a = list(input())
def string_to_binary(char_list: list) -> list[tuple]:
    list_of_tuples = []
    for i in char_list:
        list_of_tuples.append(tuple(format(ord(i), '08b')))
    return list_of_tuples