input = open("input", "r").read()


def find_index_of_first_match(buffer, key_length):
    for i in range(len(buffer)):
        current_sequence = buffer[i:(i + key_length)]
        if len(set(current_sequence)) == key_length:
            return i + key_length
    return -1


# part one
print(find_index_of_first_match(input, 4))

# part two
print(find_index_of_first_match(input, 14))
