def find_fibonacci_index_by_length(length):
    a, b = 1, 1
    index = 2
    while len(str(b)) < length:
        a, b = b, a + b
        index += 1
    return index

index = find_fibonacci_index_by_length(1000)
print(index)